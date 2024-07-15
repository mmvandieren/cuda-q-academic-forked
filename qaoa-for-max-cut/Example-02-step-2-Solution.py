# SPDX-License-Identifier: Apache-2.0 AND CC-BY-NC-4.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Defining functions to generate the Hamiltonian and Kernel for a given graph
# Necessary packages
import networkx as nx
from networkx import algorithms
from networkx.algorithms import community
import cudaq
from cudaq import spin
from cudaq.qis import *
import numpy as np
from typing import List, Tuple
from mpi4py import MPI


# Getting information about platform
cudaq.set_target("nvidia-mqpu")
target = cudaq.get_target()

# Setting up MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
num_qpus = comm.Get_size()


#######################################################
# Step 1
####################################################### 
# Function to return a dictionary of subgraphs of the input graph 
# using the greedy modularity maximization algorithm

def subgraphpartition(G,n):
    """Divide the graph up into at most n subgraphs
    
    Parameters
    ----------
    G: networkX.Graph 
        Graph that we want to subdivdie
    n : int
        n is the maximum number of subgraphs in the partition
    Returns
    -------
    dict of str : networkX.Graph
        Dictionary of networkX graphs with a string as the key
    """
    greedy_partition = community.greedy_modularity_communities(G, weight=None, resolution=1.1, cutoff=1, best_n=n)
    number_of_subgraphs = len(greedy_partition)

    graph_dictionary = {}
    graph_names=[]
    for i in range(number_of_subgraphs):
        name='G'+str(i)
        graph_names.append(name)

    for i in range(number_of_subgraphs):
        nodelist = sorted(list(greedy_partition[i]))
        graph_dictionary[graph_names[i]] = nx.subgraph(G, nodelist)
     
    return(graph_dictionary) 


if rank ==0:
    # Defining the example graph
    # Random graph parameters
    n = 35  # numnber of nodes
    m = 80  # number of edges
    seed = 20160  # seed random number generators for reproducibility

    # Use seed for reproducibility
    sampleGraph2 = nx.gnm_random_graph(n, m, seed=seed)

    # Subdividing the graph
    num_subgraphs_limit = min(12, len(sampleGraph2.nodes())) # maximum number of subgraphs for the partition
    subgraph_dictionary = subgraphpartition(sampleGraph2,num_subgraphs_limit)

    # Assign the subgraphs to the QPUs
    number_of_subgraphs = len(sorted(subgraph_dictionary))
    number_of_subgraphs_per_qpu = int(np.ceil(number_of_subgraphs/num_qpus))

    keys_on_qpu ={}
    
    for q in range(num_qpus):
        keys_on_qpu[q]=[]
        for k in range(number_of_subgraphs_per_qpu):
            if (k*num_qpus+q < number_of_subgraphs):
                key = sorted(subgraph_dictionary)[k*num_qpus+q]
                keys_on_qpu[q].append(key)        
        print(keys_on_qpu[q],'=subgraph problems to be computed on processor',q)
        

    # Distribute the subgraph data to the QPUs
    for i in range(num_qpus):
        subgraph_to_qpu ={}
        for k in keys_on_qpu[i]:
            subgraph_to_qpu[k]= subgraph_dictionary[k]
        if i != 0:
            comm.send(subgraph_to_qpu, dest=i, tag=rank)
            print("{} sent by processor {}".format(subgraph_to_qpu, rank))
        else:
            assigned_subgraph_dictionary = subgraph_to_qpu
else:
    # Receive the subgraph data
    assigned_subgraph_dictionary= comm.recv(source=0, tag=0)
    print("Processor {} received {} from processor {}".format(rank,assigned_subgraph_dictionary, 0))



#######################################################
# Step 2
####################################################### 

# Define a function to generate the Hamiltonian for a max cut problem using the graph G

def hamiltonian_max_cut(sources : List[int], targets : List[int]): 
    """Hamiltonian for finding the max cut for the graph  with edges defined by the pairs generated by source and target edges
        
    Parameters
    ----------
    sources: List[int] 
        list of the source vertices for edges in the graph
    targets: List[int]
        list of the target vertices for the edges in the graph

    Returns
    -------
    cudaq.SpinOperator
        Hamiltonian for finding the max cut of the graph defined by the given edges
    """
    hamiltonian = 0
    # Since our vertices may not be a list from 0 to n, or may not even be integers,
    
    for i in range(len(sources)):
        # Add a term to the Hamiltonian for the edge (u,v)
        qubitu = sources[i]
        qubitv = targets[i]
        hamiltonian += 0.5*(spin.z(qubitu)*spin.z(qubitv)-spin.i(qubitu)*spin.i(qubitv))
    
    return hamiltonian

# Problem Kernel

@cudaq.kernel
def qaoaProblem(qubit_0 : cudaq.qubit, qubit_1 : cudaq.qubit, alpha : float):
    """Build the QAOA gate sequence between two qubits that represent an edge of the graph
    Parameters
    ----------
    qubit_0: cudaq.qubit 
        Qubit representing the first vertex of an edge
    qubit_1: cudaq.qubit 
        Qubit representing the second vertex of an edge
    alpha: float
        Free variable   
        
    Returns
    -------
    cudaq.Kernel
        Subcircuit of the problem kernel for Max-Cut of the graph with a given edge
    """
    x.ctrl(qubit_0, qubit_1)
    rz(2.0*alpha, qubit_1)
    x.ctrl(qubit_0, qubit_1)

# Mixer Kernel
@cudaq.kernel
def qaoaMixer(qubit_0 : cudaq.qubit, beta : float):
    """Build the QAOA gate sequence that is applied to each qubit in the mixer portion of the circuit
    Parameters
    ----------
    qubit_0: cudaq.qubit 
        Qubit 
    beta: float
        Free variable   
        
    Returns
    -------
    cudaq.Kernel
        Subcircuit of the mixer kernel for Max-Cut of the graph with a given edge
    """
    rx(2.0*beta, qubit_0)


# We now define the kernel_qaoa function which will be the QAOA circuit for our graph
# Since the QAOA circuit for max cut depends on the structure of the graph, 
# we'll feed in global concrete variable values into the kernel_qaoa function for the qubit_count, layer_count, edges_src, edges_tgt.
# The types for these variables are restricted to Quake Values (e.g. qubit, int, List[int], ...)
# The thetas plaeholder will be our free parameters (the alphas and betas in the circuit diagrams depicted above)
@cudaq.kernel
def kernel_qaoa(qubit_count :int, layer_count: int, edges_src: List[int], edges_tgt: List[int], thetas : List[float]):
    """Build the QAOA circuit for max cut of the graph with given edges and nodes
    Parameters
    ----------
    qubit_count: int 
        Number of qubits in the circuit, which is the same as the number of nodes in our graph
    layer_count : int 
        Number of layers in the QAOA kernel
    edges_src: List[int]
        List of the first (source) node listed in each edge of the graph, when the edges of the graph are listed as pairs of nodes
    edges_tgt: List[int]
        List of the second (target) node listed in each edge of the graph, when the edges of the graph are listed as pairs of nodes
    thetas: List[float]
        Free variables to be optimized   
        
    Returns
    -------
    cudaq.Kernel
        QAOA circuit for Max-Cut for max cut of the graph with given edges and nodes
    """
    # Let's allocate the qubits
    qreg = cudaq.qvector(qubit_count)
    
    # And then place the qubits in superposition
    h(qreg)
    
    # Each layer has two components: the problem kernel and the mixer
    for i in range(layer_count):
        # Add the problem kernel to each layer
        for edge in range(len(edges_src)):
            qubitu = edges_src[edge]
            qubitv = edges_tgt[edge]
            qaoaProblem(qreg[qubitu], qreg[qubitv], thetas[i])
        # Add the mixer kernel to each layer
        for j in range(qubit_count):
            qaoaMixer(qreg[j],thetas[i+layer_count])
            
def find_optimal_parameters(G, layer_count, seed):
    """Function for finding the optimal parameters of QAOA for the max cut of a graph
    Parameters
    ----------
    G: networkX graph 
        Problem graph whose max cut we aim to find
    layer_count : int 
        Number of layers in the QAOA circuit
    seed : int
        Random seed for reproducibility of results
        
    Returns
    -------
    list[float]
        Optimal parameters for the QAOA applied to the given graph G
    """
    parameter_count: int = 2 * layer_count

    # Problem parameters
    nodes = sorted(list(nx.nodes(G)))
    qubit_src = []
    qubit_tgt = []
    for u, v in nx.edges(G):
        # We can use the index() command to read out the qubits associated with the vertex u and v.
        qubit_src.append(nodes.index(u))
        qubit_tgt.append(nodes.index(v))
    # The number of qubits we'll need is the same as the number of vertices in our graph
    qubit_count : int = len(nodes)
    # Each layer of the QAOA kernel contains 2 parameters
    parameter_count : int = 2*layer_count
    
    # Specify the optimizer and its initial parameters. 
    optimizer = cudaq.optimizers.COBYLA()
    np.random.seed(seed)
    optimizer.initial_parameters = np.random.uniform(-np.pi, np.pi,
                                                     parameter_count)   

    # Pass the kernel, spin operator, and optimizer to `cudaq.vqe`.
    optimal_expectation, optimal_parameters = cudaq.vqe(
        kernel=kernel_qaoa,
        spin_operator=hamiltonian_max_cut(qubit_src, qubit_tgt),
        argument_mapper=lambda parameter_vector: (qubit_count, layer_count, qubit_src, qubit_tgt, parameter_vector),
        optimizer=optimizer,
        parameter_count=parameter_count)

    return optimal_parameters
def qaoa_for_graph(G, layer_count, shots, seed):
    """Function for finding the max cut of a graph using QAOA
    
    Parameters
    ----------
    G: networkX graph 
        Problem graph whose max cut we aim to find
    layer_count : int 
        Number of layers in the QAOA circuit
    shots : int
        Number of shots in the sampling subroutine
    seed : int
        Random seed for reproducibility of results

    Returns
    -------
    str
        Binary string representing the max cut coloring of the vertinces of the graph
    """

    
    parameter_count: int = 2 * layer_count

    # Problem parameters
    nodes = sorted(list(nx.nodes(G)))
    qubit_src = []
    qubit_tgt = []
    for u, v in nx.edges(G):
        # We can use the index() command to read out the qubits associated with the vertex u and v.
        qubit_src.append(nodes.index(u))
        qubit_tgt.append(nodes.index(v))
    # The number of qubits we'll need is the same as the number of vertices in our graph
    qubit_count : int = len(nodes)
    # Each layer of the QAOA kernel contains 2 parameters
    parameter_count : int = 2*layer_count
    
    optimal_parameters = find_optimal_parameters(G, layer_count, seed)

    # Print the optimized parameters
    print("Optimal parameters = ", optimal_parameters)
    
    # Sample the circuit
    counts = cudaq.sample(kernel_qaoa, qubit_count, layer_count, qubit_src, qubit_tgt, optimal_parameters, shots_count=shots)
    print('most_probable outcome = ',counts.most_probable())
    results = str(counts.most_probable())
    return results


############################################################################
# On GPU with rank r, compute the subgraph solutions for the 
# subgraphs in assigned_subgraph_dictionary that live on GPU r
############################################################################
layer_count =1
results = {}
new_seed_for_each_graph = rank # to give each subgraph solution different initial parameters
for key in assigned_subgraph_dictionary:
    G = assigned_subgraph_dictionary[key]
    results[key] = qaoa_for_graph(G, layer_count, shots = 10000, seed=654321+new_seed_for_each_graph)
    new_seed_for_each_graph+=1
    print('The max cut QAOA coloring for the subgraph',key,'is',results[key])
print('The results dictionary variable on GPU',rank,'is',results)

############################################################################
# Exercise to copy over the subgraph solutions from the individual GPUs
# back to GPU 0.
#############################################################################
# Let's introduce another MPI function that will be useful to
# iterate over all the GPUs. 
size = comm.Get_size()

# Copy the results over to QPU 0 for consolidation 
if rank!=0:
    comm.send(results, dest=0, tag=0)
    print("{} sent by processor {}".format(results, rank))
else:
    for j in range(1,size,1):
        colors = comm.recv(source=j, tag=0)
        print("Received {} from processor {}".format(colors, j))
        for key in colors:
            results[key]=colors[key]
    print("The results dictionary on GPU 0 =", results)
 
