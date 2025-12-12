# 🎓 CUDA-Q Interactive Widget Catalog

## Visual Tools for Quantum Education

Welcome to the **CUDA-Q Interactive Widget Catalog**. This collection offers interactive HTML visualizations designed to demonstrate core quantum computing concepts.

These widgets are general-purpose. While they may originate from specific domain examples (like Chemistry or Finance), they demonstrate universal mechanics—such as superposition, optimization, and unitary evolution—that are applicable across Physics, Computer Science, and Mathematics.

### Adapt these tools for your classroom
These widgets are open source. We encourage you to not only use them as-is but to adapt the code.
* **Launch:** Click to view the interactive widget in your browser immediately.
* **Source:** Click to view the HTML source code on GitHub.
* **Context:** Click the "Original Module" link to see how this widget was used in a full lesson plan.

---

## 1. Fundamentals & Qubit Visualization
*Visualizations for single-qubit states, superposition, and measurement logic.*

| Widget | Description | Original Module (Context) | Links |
| :--- | :--- | :--- | :--- |
| **Bloch Sphere Visualizer** | Interactive 3D representation of a quantum state. Allows users to visualize state vectors, phase changes, and the geometric difference between bit-flips and phase-flips. | [Quick Start to Quantum Computing](https://github.com/NVIDIA/cuda-q-academic/tree/main/quick-start-to-quantum) | [🚀 Launch](https://nvidia.github.io/cuda-q-academic/quantum-applications-to-finance/images/bloch_sphere_visualization.html) <br> [📄 Source](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/quantum-applications-to-finance/images/bloch_sphere_visualization.html) |
| **Quantum Coin Flip** | A comparative visualization of a Classical Coin (bit) versus a Quantum Coin (qubit). Demonstrates the Hadamard gate, superposition, phase, and probability amplitudes. | [Applications to Finance](https://github.com/NVIDIA/cuda-q-academic/tree/main/quantum-applications-to-finance) | [🚀 Launch](https://nvidia.github.io/cuda-q-academic/quantum-applications-to-finance/images/quantum_coin_widget.html) <br> [📄 Source](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/quantum-applications-to-finance/images/quantum_coin_widget.html) |

---

## 2. Gates, Matrices, & Circuit Logic
*Tools for visualizing linear algebra, operators, and circuit construction.*

| Widget | Description | Original Module (Context) | Links |
| :--- | :--- | :--- | :--- |
| **Unitary Matrix Visualizer** | Interactive visualization of Unitary matrices. Demonstrates how quantum gates operate as rotations that preserve probability norms in a vector space. | [AI for Quantum](https://github.com/NVIDIA/cuda-q-academic/tree/main/ai-for-quantum) | [🚀 Launch](https://nvidia.github.io/cuda-q-academic/ai-for-quantum/widgets/unitary_widget.html) <br> [📄 Source](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/ai-for-quantum/widgets/unitary_widget.html) |
| **Gate Logic Widget** | An interactive "sandbox" for quantum logic gates. Users can visualize the specific inputs and outputs of various gates to understand reversible computing logic. | [Quick Start to Quantum Computing](https://github.com/NVIDIA/cuda-q-academic/tree/main/quick-start-to-quantum) | [🚀 Launch](https://nvidia.github.io/cuda-q-academic/quantum-applications-to-finance/images/gate-widget.html) <br> [📄 Source](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/quantum-applications-to-finance/images/gate-widget.html) |

---

## 3. Stochastic Processes & Search Algorithms
*Visualizations of random walks, diffusion, and graph traversal.*

| Widget | Description | Original Module (Context) | Links |
| :--- | :--- | :--- | :--- |
| **Classical Random Walk** | Visualizes a 1D walk where the walker's movement is determined by a coin flip. | [Applications to Finance](https://github.com/NVIDIA/cuda-q-academic/tree/main/quantum-applications-to-finance) | [🚀 Launch](https://nvidia.github.io/cuda-q-academic/quantum-applications-to-finance/images/random_walk.html) <br> [📄 Source](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/quantum-applications-to-finance/images/random_walk.html) |
| **Split Step Random Walk** | A variation of the classical random walk in which each step is split into two decisions: move left or stay put and then move right or stay put. | [Quick Start to Quantum Computing](https://github.com/NVIDIA/cuda-q-academic/tree/main/quick-start-to-quantum) | [🚀 Launch](https://nvidia.github.io/cuda-q-academic/quantum-applications-to-finance/images/ss-random-walk.html) <br> [📄 Source](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/quantum-applications-to-finance/images/ss-random-walk.html) |
| **Diffusion Model** | Visualizes the diffusion process. Demonstrates how noise is added or removed from data, a key concept in both thermodynamics and modern generative AI models. | [AI for Quantum](https://github.com/NVIDIA/cuda-q-academic/tree/main/ai-for-quantum) | [🚀 Launch](https://nvidia.github.io/cuda-q-academic/ai-for-quantum/widgets/diffusion.html) <br> [📄 Source](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/ai-for-quantum/widgets/diffusion.html) |

---

## 4. Optimization & Variational Algorithms
*Demonstrations of hybrid quantum-classical loops and cost function minimization.*

| Widget | Description | Original Module (Context) | Links |
| :--- | :--- | :--- | :--- |
| **VQE Convergence** | Dynamically visualizes the Variational Quantum Eigensolver (VQE) algorithm, showing how an optimizer iteratively updates parameters to find the minimum value (ground state). | [Chemistry Simulations](https://github.com/NVIDIA/cuda-q-academic/tree/main/chemistry-simulations) | [🚀 Launch](https://nvidia.github.io/cuda-q-academic/chemistry-simulations/Images/VQE_Widget.html) <br> [📄 Source](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/chemistry-simulations/Images/VQE_Widget.html) |
| **QUBO / Graph Solver** | Visualizes the solution to a Quadratic Unconstrained Binary Optimization (QUBO) problem, often used for combinatorial optimization tasks. | [Applications to Finance](https://github.com/NVIDIA/cuda-q-academic/tree/main/quantum-applications-to-finance) | [🚀 Launch](https://nvidia.github.io/cuda-q-academic/quantum-applications-to-finance/images/QUBO_widget.html) <br> [📄 Source](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/quantum-applications-to-finance/images/QUBO_widget.html) |
| **Q-CHOP vs Adiabatic** | An animated comparison of two optimization approaches: standard adiabatic evolution versus a "chopped" or QAOA-style ansatz, comparing convergence speed and quality. | [Applications to Finance](https://github.com/NVIDIA/cuda-q-academic/tree/main/quantum-applications-to-finance) | [🚀 Launch](https://nvidia.github.io/cuda-q-academic/quantum-applications-to-finance/images/Q_CHOP_Animated.html) <br> [📄 Source](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/quantum-applications-to-finance/images/Q_CHOP_Animated.html) |
| **ADAPT-VQE** | Demonstrates an adaptive algorithm that constructs its own ansatz (circuit architecture) iteratively, adding operators one by one to minimize energy. | [Chemistry Simulations](https://github.com/NVIDIA/cuda-q-academic/tree/main/chemistry-simulations) | [🚀 Launch](https://nvidia.github.io/cuda-q-academic/chemistry-simulations/Images/adapt_vqe/adapt_widget.html) <br> [📄 Source](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/chemistry-simulations/Images/adapt_vqe/adapt_widget.html) |

---

## 5. Advanced System Simulation & Approximation
*Visualizations for numerical methods, dimensionality reduction, and system modeling.*

| Widget | Description | Original Module (Context) | Links |
| :--- | :--- | :--- | :--- |
| **Krylov Subspace** | Visualizes Krylov subspace methods, which are used to approximate eigenvalues of large sparse matrices or simulate time evolution in complex systems. | [Chemistry Simulations](https://github.com/NVIDIA/cuda-q-academic/tree/main/chemistry-simulations) | [🚀 Launch](https://nvidia.github.io/cuda-q-academic/chemistry-simulations/Images/krylov.html) <br> [📄 Source](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/chemistry-simulations/Images/krylov.html) |
| **Active Space Selection** | Visualizes the concept of "Active Space" selection—choosing a subset of variables (orbitals) to simulate while freezing others—demonstrating approximation methods. | [Chemistry Simulations](https://github.com/NVIDIA/cuda-q-academic/tree/main/chemistry-simulations) | [🚀 Launch](https://nvidia.github.io/cuda-q-academic/chemistry-simulations/Images/activespace.html) <br> [📄 Source](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/chemistry-simulations/Images/activespace.html) |
| **Hybrid System (QM/MM)** | Visualizes a multi-scale simulation where a specific quantum region is embedded within a larger classical environment (QM/MM). | [Chemistry Simulations](https://github.com/NVIDIA/cuda-q-academic/tree/main/chemistry-simulations) | [🚀 Launch](https://nvidia.github.io/cuda-q-academic/chemistry-simulations/Images/qmmm_widget.html) <br> [📄 Source](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/chemistry-simulations/Images/qmmm_widget.html) |