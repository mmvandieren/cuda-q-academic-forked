# CUDA-Q Academic 


This repository contains Jupyter notebooks and supporting files for [quantum computing](https://www.nvidia.com/en-us/solutions/quantum-computing/) training using CUDA-Q.  These training materials have been developed by NVIDIA Corporation and are provided free of charge. Please see [LICENSE](LICENSE) for license details.

Instructions to install CUDA-Q can be found in the [instructions.md](instructions.md) file. If you do not have a local installation of CUDA-Q running on a GPU, the notebooks can be opened in qBraid Lab, CoCalc, or in Google Colab. Simply  click on the Launch on the icons below or navigate to the notebook in github and select the respective icons at the top of the page.  Note that using Google Colab will require additional steps outlined in the notebooks to install CUDA-Q. 

[<img src="https://qbraid-static.s3.amazonaws.com/logos/Launch_on_qBraid_white.png" width="150">](https://account.qbraid.com?gitHubUrl=https://github.com/NVIDIA/cuda-q-academic.git)
If using qBraid Lab, use the [Environment Manager](https://docs.qbraid.com/lab/user-guide/environments) to install the CUDA-Q environment and then activate it in your notebook. In qBraid Lab you can switch to a GPU instance using the [Compute Manager](https://docs.qbraid.com/lab/user-guide/compute-manager).

# CUDA-Q Educational Resources 
* The [sample syllabus](Sample-Syllabus.md) is intended to assist faculty or students in identifying CUDA-Q resources that align with their quantum information science or quantum computing syllabi or learning path.

* The [Guide to CUDA-Q Backends](Guide-to-cuda-q-backends.ipynb) is a one-stop resource for code snippets and descriptions of the CUDA-Q backend simulator and hardware options for executing CUDA-Q kernels.
  
* CUDA-Q Acadmeic Learning Paths: These learning paths contain interactive notebooks leverage CUDA-Q to teach quantum computing concepts, applications, and algorithms. They also cover essential high-performance computing skills required for hybrid quantum-classical programming.

[](/images/learning-paths.png)

# Navigating the Learning Paths
You can browse the notebooks in this repository or follow one of the suggested learning paths in the image above. The notebooks are organized in folders in the respository as follows:

## Quick Start to Quantum Computing with CUDA-Q
The Quick Start to Quantum Computing with CUDA-Q is a great place to start for those new to quantum computing or CUDA-Q. The folder titled `quick-start-to-quantum` contains the Quick Start to Quantum Computing with CUDA-Q module which aims to take a learner from no knowledge of quantum computation to programming a variational algorithm in CUDA-Q. This material, which includes Jupyter notebooks, is organized into labs that build upon one another. After completing the notebooks in this module you will be ready to explore more advanced examples in the other folders of this repository. 

Pre-requisites:
* Familiarity with Python and Jupyter notebooks
* Familiarity with linear algebra, statistics, and basic complex number arithmetic 

## Accelerating Quantum Computing with Circuit Cutting: Divide and Conquer QAOA for Max Cut
The folder titled `qaoa-for-max-cut` contains a series of notebooks and Python scripts that introduce circuit cutting through a concrete example of the max cut problem. The goal of these labs is to apply a divide-and-conquer QAOA algorithm to a large max cut problem using parallel computation. [Lab 0](qaoa-for-max-cut/00_StartHere.ipynb) gives an overview of the learning material and an introduction to working with the Jupyter notebooks. [Labs 1](qaoa-for-max-cut/01_Max-Cut-with-QAOA.ipynb), [2](qaoa-for-max-cut/02_One_level_divide_and_conquer_QAOA.ipynb), and [3](qaoa-for-max-cut/03_Recursive-divide-and-conquer.ipynb) provide instructional material including solutions to exercises, while [Lab 4](qaoa-for-max-cut/04_Assessment.ipynb) can serve as an open-ended assessment.

Pre-requisites: Quick Start to Quantum Computing with CUDA-Q or equivalently familiarty with variational quantum algorithms 

## Quantum Walks for Finance Applications
This series of notebooks introduces students to the problem of loading a probability distribution into a quantum state.  Students explore discrete time quantum walks, split step quantum walks, and multi-split-step quantum walks and discover how to apply these to a problem of Eurpoean options pricing.

Pre-requisites: Quick Start to Quantum Computing with CUDA-Q or equivalently familiarty with variational quantum algorithms. 

## AI for Quantum
This series of notebooks is currently under development.  The first notebook available introduces students to the problem of compiling 

Pre-requisites: Quick Start to Quantum Computing with CUDA-Q Notebooks 1 and 2. Familiarity with generative AI, such as the [Deep Learning Institute Generative AI with Diffusion Models course](https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-FX-14+V1) [available for free for a limited time using this link](https://sp-events.courses.nvidia.com/dli-india25?ncid=ref-inpa-419622)

## Quantum Error Correction
This series of notebooks is currently under development.  The first two notebooks are available and introduces students to the basics of quantum error correction and the CUDA-Q Quantum Error Correction library.

Pre-requisites: Quick Start to Quantum Computing with CUDA-Q Notebooks 1 and 2.

## Conference Presentations
The conference presentations folder contains tutorial notebooks presented at conferences and workshops.  These are not maintained, so look in the folders above for the most recent versions.

