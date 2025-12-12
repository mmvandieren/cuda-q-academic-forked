# 🎓 CUDA-Q Interactive Widget Catalog

## Bring Your Quantum Curriculum to Life

Welcome to the **CUDA-Q Interactive Widget Catalog**. This collection is designed to help you transform abstract quantum theory into tangible, visual learning experiences for your students.

While some of these tools were originally built for specific subjects (like Finance or Chemistry), they are built on universal quantum concepts. **We encourage you to "borrow" widely:** a random walk visualization from Finance is perfect for a Computer Science algorithms class, and an optimization widget from Chemistry is an excellent way to teach gradient descent in Mathematics.

**How to use this catalog:**
* **Browse by Concept:** Find the teaching moment you need (e.g., "Superposition," "Optimization," "Linear Algebra").
* **Click & Teach:** The links below take you directly to the live, interactive widget. No installation required—just open them in your browser and share your screen.

---

## 1. Fundamentals & Qubit Visualization
*Best for: Intro to Quantum Computing, Linear Algebra, Physics*

These widgets provide the foundational "Hello World" moments for students, visualizing the behavior of single qubits, superposition, and measurement logic.

| Widget | Core Concept | How to use this in your class | Live Link |
| :--- | :--- | :--- | :--- |
| **Bloch Sphere Visualizer** | State Vectors ($\psi$) | **The essential visual.** Use this to demonstrate state vectors, phase, and the geometry of a qubit. It allows students to rotate the sphere and visualize bit-flips vs. phase-flips intuitively. | [Launch Widget](https://nvidia.github.io/cuda-q-academic/quantum-applications-to-finance/images/bloch_sphere_visualization.html) |
| **Quantum Coin Flip** | Superposition | **The perfect ice-breaker.** Compare a deterministic Classical Coin against a Quantum Coin. Use this to visually explain the Hadamard gate, interference, and probability amplitudes without heavy math. | [Launch Widget](https://nvidia.github.io/cuda-q-academic/quantum-applications-to-finance/images/quantum_coin_widget.html) |

---

## 2. Gates, Matrices, & Circuit Logic
*Best for: Computer Science, Logic & Design, Linear Algebra*

Tools for understanding how operators change state and how circuits are constructed.

| Widget | Core Concept | How to use this in your class | Live Link |
| :--- | :--- | :--- | :--- |
| **Unitary Matrix Visualizer** | Linear Algebra | **Math made visible.** Move beyond static equations. Show students how quantum gates act as rotations that preserve probability norms. Great for visualizing what "Unitary" actually looks like. | [Launch Widget](https://nvidia.github.io/cuda-q-academic/ai-for-quantum/widgets/unitary_widget.html) |
| **Gate Logic Widget** | Circuit Composition | **Interactive Sandbox.** A simple interface for inputs and outputs of various quantum gates. Use this in "Logic & Design" courses to demonstrate reversible computing and gate truth tables. | [Launch Widget](https://nvidia.github.io/cuda-q-academic/quantum-applications-to-finance/images/gate-widget.html) |

---

## 3. Stochastic Processes & Search Algorithms
*Best for: Algorithms (CS), Finance, Statistical Physics*

Dynamic visualizations of movement through graphs, probability distributions, and diffusion.

| Widget | Core Concept | How to use this in your class | Live Link |
| :--- | :--- | :--- | :--- |
| **1D Random Walk** | Stochastic Processes | **Visualizing volatility.** Whether you are teaching market movement in **Finance** or search algorithms in **CS**, this widget compares classical Brownian motion with quantum walks. | [Launch Widget](https://nvidia.github.io/cuda-q-academic/quantum-applications-to-finance/images/random_walk.html) |
| **Steady-State / Spatial Search** | Graph Theory | **Graph Traversal.** A variation of the walk often used to demonstrate how quantum algorithms traverse graphs or find marked nodes faster than classical counterparts. | [Launch Widget](https://nvidia.github.io/cuda-q-academic/quantum-applications-to-finance/images/ss-random-walk.html) |
| **Diffusion Model** | Generative Processes | **Thermodynamics & AI.** Visualizes the diffusion process. Highly relevant for **Physics** (entropy/thermodynamics) and **Modern AI** courses explaining how diffusion models (like Stable Diffusion) work. | [Launch Widget](https://nvidia.github.io/cuda-q-academic/ai-for-quantum/widgets/diffusion.html) |

---

## 4. Optimization & Variational Algorithms
*Best for: Machine Learning, Operations Research, Calculus*

These widgets demonstrate "Hybrid Quantum-Classical" loops, where a classical optimizer tunes a quantum circuit to find the lowest energy (or cost).

| Widget | Core Concept | How to use this in your class | Live Link |
| :--- | :--- | :--- | :--- |
| **VQE Convergence** | Cost Function Optimization | **Calculus in action.** Dynamically shows an optimizer "rolling down the hill" to find a minimum. Perfect for teaching **Gradient Descent** or hybrid optimization techniques in any field. | [Launch Widget](https://nvidia.github.io/cuda-q-academic/chemistry-simulations/Images/VQE_Widget.html) |
| **QUBO / Graph Solver** | Combinatorial Optimization | **Solving the impossible.** Visualizes solving a Quadratic Unconstrained Binary Optimization problem. Use this for **Logistics** (Traveling Salesman), **Finance** (Portfolio), or **CS** (Max-Cut) problems. | [Launch Widget](https://nvidia.github.io/cuda-q-academic/quantum-applications-to-finance/images/QUBO_widget.html) |
| **Q-CHOP vs Adiabatic** | Annealing vs. QAOA | **Algorithm Face-off.** Compares adiabatic evolution (slow & steady) against chopped/QAOA style optimization. Excellent for comparing algorithm performance and convergence speeds. | [Launch Widget](https://nvidia.github.io/cuda-q-academic/quantum-applications-to-finance/images/Q_CHOP_Animated.html) |
| **ADAPT-VQE** | Adaptive Architecture | **Self-building circuits.** Shows an algorithm that "grows" its own circuit structure operator-by-operator. A great conceptual analog for **Neural Architecture Search** in ML courses. | [Launch Widget](https://nvidia.github.io/cuda-q-academic/chemistry-simulations/Images/adapt_vqe/adapt_widget.html) |

---

## 5. Advanced System Simulation & Approximation
*Best for: Computational Physics, Numerical Methods, Data Science*

Tools for visualizing how we simplify complex, high-dimensional problems to make them solvable.

| Widget | Core Concept | How to use this in your class | Live Link |
| :--- | :--- | :--- | :--- |
| **Krylov Subspace** | Sparse Matrices / Time | **Approximation methods.** Visualizes Krylov methods. Essential for **Numerical Analysis** classes teaching how to approximate eigenvalues of massive matrices or simulate time evolution. | [Launch Widget](https://nvidia.github.io/cuda-q-academic/chemistry-simulations/Images/krylov.html) |
| **Active Space Selection** | Dimensionality Reduction | **Feature Selection.** Visualizes selecting specific meaningful variables (orbitals) and ignoring others. Use this in **Data Science** to explain dimensionality reduction or in **Physics** for approximation. | [Launch Widget](https://nvidia.github.io/cuda-q-academic/chemistry-simulations/Images/activespace.html) |
| **Hybrid System (QM/MM)** | Boundary Conditions | **Multiscale Modeling.** Shows a small quantum system embedded in a larger classical environment. Useful for **Systems Engineering** or **Multiscale Physics** modeling. | [Launch Widget](https://nvidia.github.io/cuda-q-academic/chemistry-simulations/Images/qmmm_widget.html) |