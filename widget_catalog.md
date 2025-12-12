# CUDA-Q Interactive Widget Catalog (By Concept)

This catalog organizes available HTML widgets by **learning objective**. While some of these widgets were originally developed for specific domains (like Finance or Chemistry), their underlying mechanics demonstrate universal quantum computing concepts applicable to Physics, Computer Science, and Mathematics curriculums.

## 1. Fundamentals & Qubit Visualization
*Best for: Intro to Quantum Computing, Linear Algebra, Physics*

These widgets help students visualize the behavior of single qubits, superposition, and measurement.

| Widget | Concept | General Application | Link |
| :--- | :--- | :--- | :--- |
| **Bloch Sphere Visualizer** | State Vectors | The standard tool for visualizing a qubit's state ($\psi$), phase, and bit-flip/phase-flip channels. Essential for all introductory courses. | [View Widget](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/quantum-applications-to-finance/images/bloch_sphere_visualization.html) |
| **Quantum Coin Flip** | Superposition | A comparative visualization of a Classical Coin (deterministic/random) vs. a Quantum Coin (Hadamard gate/Superposition). Great for explaining interference and probability amplitudes. | [View Widget](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/quantum-applications-to-finance/images/quantum_coin_widget.html) |

---

## 2. Gates, Matrices, & Circuit Logic
*Best for: Computer Science, Circuit Design, Linear Algebra*

Tools for understanding how operators change state and how circuits are constructed.

| Widget | Concept | General Application | Link |
| :--- | :--- | :--- | :--- |
| **Unitary Matrix Visualizer** | Linear Algebra | Interactive visualization of Unitary matrices. Helps students understand how quantum gates act as rotations that preserve probability norms, regardless of the application domain. | [View Widget](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/ai-for-quantum/widgets/unitary_widget.html) |
| **Gate Logic Widget** | Circuit Composition | A sandbox for seeing inputs and outputs of various quantum gates. Useful for "Logic & Design" courses to demonstrate reversible computing. | [View Widget](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/quantum-applications-to-finance/images/gate-widget.html) |

---

## 3. Stochastic Processes & Search Algorithms
*Best for: Algorithms (CS), Finance, Statistical Physics*

Visualizations of movement through graphs and probability distributions.

| Widget | Concept | General Application | Link |
| :--- | :--- | :--- | :--- |
| **1D Random Walk** | Stochastic Processes | Visualizes a quantum particle moving in 1D. Applicable to **CS** (the basis of Grover's search/Spatial Search), **Finance** (market volatility), and **Physics** (particle diffusion). | [View Widget](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/quantum-applications-to-finance/images/random_walk.html) |
| **Steady-State / Spatial Search** | Graph Theory | A variation of the walk often used to demonstrate how quantum algorithms traverse graphs faster than classical ones. | [View Widget](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/quantum-applications-to-finance/images/ss-random-walk.html) |
| **Diffusion Model** | Generative Processes | Visualizes the diffusion process. While labeled for AI, this is highly relevant for **Physics** (thermodynamics) and **Math** (differential equations). | [View Widget](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/ai-for-quantum/widgets/diffusion.html) |

---

## 4. Optimization & Variational Algorithms
*Best for: Machine Learning, Operations Research, Advanced Chemistry*

These widgets demonstrate "Hybrid Quantum-Classical" loops, where a classical optimizer tunes a quantum circuit.

| Widget | Concept | General Application | Link |
| :--- | :--- | :--- | :--- |
| **VQE Convergence** | Cost Function Optimization | dynamically shows a Variational Quantum Eigensolver finding a minimum. Generic application: Teaching any **Gradient Descent** or hybrid optimization technique. | [View Widget](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/chemistry-simulations/Images/VQE_Widget.html) |
| **QUBO / Graph Solver** | Combinatorial Optimization | Visualizes solving a Quadratic Unconstrained Binary Optimization problem. Applicable to **Logistics** (Traveling Salesman), **Finance** (Portfolio), and **CS** (Max-Cut problems). | [View Widget](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/quantum-applications-to-finance/images/QUBO_widget.html) |
| **Q-CHOP vs Adiabatic** | Annealing vs. QAOA | Compares adiabatic evolution (slowly changing Hamiltonians) against chopped/QAOA style optimization. Good for comparing different algorithm classes. | [View Widget](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/quantum-applications-to-finance/images/Q_CHOP_Animated.html) |
| **ADAPT-VQE** | Adaptive Ansatz | Shows an algorithm that "grows" its own circuit structure. Excellent for **Machine Learning** courses discussing adaptive model architecture. | [View Widget](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/chemistry-simulations/Images/adapt_vqe/adapt_widget.html) |

---

## 5. Advanced System Simulation & Approximation
*Best for: Computational Physics, Numerical Methods*

Tools for visualizing how we simplify complex problems to make them solvable.

| Widget | Concept | General Application | Link |
| :--- | :--- | :--- | :--- |
| **Krylov Subspace** | Sparse Matrices / Time | Visualizes Krylov methods. Essential for **Numerical Analysis** classes teaching how to approximate eigenvalues of massive matrices or simulate time evolution. | [View Widget](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/chemistry-simulations/Images/krylov.html) |
| **Active Space (Approximation)** | Dimensionality Reduction | Visualizes selecting specific meaningful variables (orbitals) and ignoring others. Applicable to **Data Science** (feature selection) and **Physics**. | [View Widget](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/chemistry-simulations/Images/activespace.html) |
| **Hybrid System (QM/MM)** | Boundary Conditions | Shows a small quantum system embedded in a larger classical environment. Useful for **Systems Engineering** or **Multiscale Physics** modeling. | [View Widget](https://github.com/NVIDIA/cuda-q-academic/blob/widgets-as-html/chemistry-simulations/Images/qmmm_widget.html) |