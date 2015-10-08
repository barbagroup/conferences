## Session Title
------------------------

Explore AmgX and use it to acclerate PETSc-based immersed-boundary method CFD codes

## Contact
------------------------

Pi-Yueh Chuang
PhD Student, George Washington University

## Format
------------------------

25-minute Talk

## Audience Level
------------------------

All

## Topics
------------------------

* Computational Fluid Dynamics
* Supercomputing and HPC
* Programming Language

## Other Topic
------------------------

## Session Description
------------------------

This presentation is co-authored with Professor Lorena Barba. In this session, we will show how to apply AmgX -- a NVIDIA experimental library of multi-GPU linear solvers with multigrid preconditioners -- to and accelerate existing PETSc applications. We will show the wrapper we developed for AmgX against PETSc. With this wrapper, programmers can easily apply AmgX solvers to their existing parallel programs that use PETSc KSP solvers by just adding less than 10 lines to the codes. An example using PetIBM -- our PETSc-based scalable immersed-boundary method CFD codes -- will demonstrate how AmgX can immediately accelerate the application and how its multi-GPU capacity can be useful for large-scale 3D CFD simulations. We will also present the performance benchmarks of AmgX and the strategies for optimizing multigrid preconditioners on GPUs, which are sometimes different from how we set them on CPU-based multigrid preconditioners. 

## Extended Abstract & Results
------------------------

Our works aim to easily accelerate our immersed-boundary-method CFD codes -- PetIBM, a scalable codes parallelized using PETSc -- without much pain and many modifications on source codes. We pick AmgX for our GPU solvers because its multi-GPU capacity can break the memory limit of a single GPU. We develop a wrapper for AmgX and PETSc to ease the collaboration between them. Before using AmgX in PetIBM, we first explore the performance of AmgX by using 2D and 3D Poisson problems and compare results to the PETSc KSP solvers. The benchmark shows good speed up can be achieved. For example, using AmgX with different numbers and models of GPUs to solve a 3D Poisson problem against using PETSc KSP solver and a 32-CPU cluster shows speed up of: 5x~15x with 1~16 K20m GPUs and 4M unknowns; 2x with 1 old-generation C2050 and 2M unknowns; and 6~8x with 1~2 K40 GPUs and 8M unknowns. By the benchmark, we also found that the optimized parameters for the multigrid preconditioners not only depend on the problems to solve but also number of GPUs and model of GPUs. For example, PMIS selector may be good enough for 1 GPU while HMIS selector may be better for 4 GPUs. Strategies to set CPU-based multigrid preconditioners may also differ from those on GPUs. For instance, F and W cycle may be useful on CPU-based solvers, while the simplest V cycle is more suitable for GPU solvers because solving coarsest-grid system is relatively expansive on GPUs. We are looking forward more systematical benchmarks in order to get more sense and strategies about how to efficiently use AmgX. After benchmarks of AmgX, we will also present the speed up of PetIBM after adopting AmgX. In PetIBM, solving Poisson system costs 90% of time when using CPUs. We expect to have a significant speed up of using AmgX. Also, with the multi-GPU capacity, we can now solve larger scale problems or have finer grid resolutions to carry out turbulent flow simulations on GPUs.

## Presenter Public Speaking History
------------------------
The author is one of the members in Professor Lorena Barba's group. Previous experience of author's speaking history is:

Presentation for paper competition, 19th National Computational Fluid Dynamic Conference, Penghu, Taiwan, 2012


