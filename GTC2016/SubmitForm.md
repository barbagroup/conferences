## Session Title
------------------------

Using AmgX to accelerate PETSc-based CFD codes

## Contact
------------------------

Pi-Yueh Chuang
PhD Student, George Washington University

## Format
------------------------

25-minute Talk

## Audience Level
------------------------

Intermediate

## Topics
------------------------

* Computational Fluid Dynamics
* Supercomputing and HPC

## Other Topic
------------------------

## Session Description
------------------------

Learn to accelerate existing PETSc applications using AmgX–NVIDIA's library of multi-GPU linear solvers and multigrid preconditioners. We developed wrapper code to couple AmgX and PETSC, allowing programmers to use it with fewer than 10 additional lines of code. Using PetIBM, our PETSc-based immersed-boundary CFD solver, we show how AmgX can speed up an application with little programming effort. AmgX can thus bring multi-GPU capability to large-scale 3D CFD simulations, reducing execution time and lowering hardware costs. As example, we estimate the potential cost savings using Amazon AWS compute cloud. We also present performance benchmarks of AmgX, and tips for optimizing GPU multigrid preconditioners for CFD. This presentation is co-authored with Professor Lorena A. Barba.

## Extended Abstract & Results
------------------------

This work aims to accelerate our immersed boundary method CFD solver (PetIBM), without too much pain or substantial code modification.
We chose AmgX as our GPU solvers because of its multi-GPU capability. Our CFD solver already uses the PETSc library, which meant we had to develop wrapper code to couple the two.
We first explore the performance of AmgX on 2D and 3D Poisson problems and compare the results to PETSc KSP solvers.
Our benchmarks show AmgX can achieve respectable speed ups. For example, using 1 to 16 K20m GPUs to solve a 3D Poisson problem with AmgX on 4M unknowns results in a speed up of betwee 5x and 15x compared to using PETSc KSP solvers on 32 CPU cores (2 nodes). For larger problems, using AmgX on 32 K20m GPUs with 100M unknowns results in speed-ups of 62x, 26x, and 9x compared to PETSc on 128, 256, and 512 CPU cores.
Even using only one C2050, an old-generation GPU, results in a 2x speed-up compared to PETSc on 32 CPU cores. Solving larger problems on GPUs is limited by the memory on each GPU card.
We also show how optimal choices of parameters for multigrid preconditioners depend not only on the problem but also on the number and model of GPUs. 
Strategies to set parameters diffe whether using GPU-or CPU-based multigrid preconditioners. For instance, F and W cycles may be useful on CPUs, while the simplest V cycle may be more suitable on GPUs, because solving on the coarsest-grid is proportionally more expensive on GPUs.
We are conducting more systematic benchmarks in order to give users a better sense of how to get good performance with AmgX.
In our application code (PetIBM), solving the Poisson system with PETSc KSP solvers takes up to 90% of the execution time.
We expect a significant speed-up with AmgX. On multiple GPUs, we can solve larger-scale problems or have finer grids to carry out turbulent flow simulations.
Using AmgX can lower overall hardware cost for a given application. With Amazon AWS, for example: if we wanted to solve the problem mentioned above, with 100M unknowns on 512 CPU cores, it would cost about $28 per hour; whereas solving it on a 32-GPU cluster using AmgX would cost about $20 per hour. More importantly, the execution time required on the 32-GPU cluster could be 9x less (extrapolating from our tests). We plan to confirm a large saving on the cost of running PetIBM with AmgX on cloud compute resources.

## Presenter Public Speaking History
------------------------
The presenter is a member in Professor Lorena Barba's research group and he will be mentored by Prof. Barba for this session. The presenter's speaking history is:
Presentation for paper competition, 19th National Computational Fluid Dynamic Conference, Penghu, Taiwan, 2012.


