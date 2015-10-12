## Session Title
------------------------

Using AmgX to Accelerate PETSc-Based CFD Codes

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

Learn to accelerate existing PETSc applications using AmgX–NVIDIA's library of multi-GPU linear solvers and multigrid preconditioners. 
We developed wrapper code to couple AmgX and PETSc, allowing programmers to use it with fewer than 10 additional lines of code. 
Using PetIBM, our PETSc-based immersed-boundary CFD solver, we show how AmgX can speed up an application with little programming effort. 
AmgX can thus bring multi-GPU capability to large-scale 3D CFD simulations, reducing execution time and lowering hardware costs. 
As example, we estimate the potential cost savings using Amazon elastic compute cloud (EC2). 
We also present performance benchmarks of AmgX, and tips for optimizing GPU multigrid preconditioners for CFD. 
This presentation is co-authored with Professor Lorena A. Barba.

## Extended Abstract & Results
------------------------

This work aims to accelerate our immersed boundary method CFD solver (PetIBM), without too much pain or substantial code modification.
We chose AmgX as our GPU solvers because of its multi-GPU capability. 
Our CFD solver already uses the PETSc library, which meant we had to develop wrapper code to couple the two.
We first explore the performance of AmgX on 2D and 3D Poisson problems and compare the results to PETSc KSP solvers.
Our benchmarks show AmgX can achieve respectable speed-ups. 
For example, using 1 to 16 K20m GPUs to solve a 3D Poisson problem with AmgX on 4M unknowns results in a speed-up of between 5x and 15x compared to using PETSc KSP solvers on 32 CPU cores (2 nodes). 
For larger problems, using AmgX on 32 K20m GPUs with 100M unknowns results in speed-ups of 62x, 26x, and 9x compared to PETSc on 128, 256, and 512 CPU cores.
Even using only one C2050, an old-generation GPU, results in a 2x speed-up compared to PETSc on 32 CPU cores. 
We will also show how optimal choices of parameters for multigrid preconditioners depend not only on the problem but also on the number and model of GPUs. 
Strategies to set parameters differ whether using GPU-or CPU-based multigrid preconditioners. 
For instance, F and W cycles may be useful on CPUs, while the simplest V cycle may be more suitable on GPUs, because solving on the coarsest grid is proportionally more expensive on GPUs.
We are conducting more systematic benchmarks in order to give users a better sense of how to get good performance with AmgX.
In our application code (PetIBM), solving the Poisson system with PETSc KSP solvers takes up to 90% of the execution time.
We expect a significant speed-up with AmgX. 
On multiple GPUs, we can solve larger-scale problems or have finer grids to carry out turbulent flow simulations.
Using AmgX can lower overall hardware cost for a given application. 
With Amazon AWS, for example: if we wanted to solve the problem mentioned above, with 100M unknowns on 512 CPU cores, it would cost about $28 per hour; whereas solving it on a 32-GPU cluster using AmgX would cost about $20 per hour. 
More importantly, the execution time required on the 32-GPU cluster could be 9x less (extrapolating from our tests). 
We plan to confirm a large saving on the cost of running PetIBM with AmgX on cloud compute resources.

## Presenter Public Speaking History
------------------------
The presenter is a member in Professor Lorena A. Barba's research group. 
Prof. Barba presented a session at GTC in years 2010, 2013, and 2014 and is a highly rated speaker.
The presenter will be mentored by Prof. Barba for this session.

The presenter's speaking history is:  
"A study of the lattice thermal conductivity of 3D nanoparticle composites", peper compitition at 19th National Computational Fluid Dynamic Conference, Penghu, Taiwan, 2012.

## Presenters
------------------------

**First Name**: Lorena  
**Last Name**: Barba  
**Email**: labarba@gwu.edu  
**Cell Phone**: 617-909-5900  
**Job Title**: Associate Professor  
**Company**: George Washington University  
**Biography**: 
Lorena A. Barba is Associate Professor of Mechanical and Aerospace Engineering at the George Washington University, in Washington DC. 
She has MSc and PhD degrees in Aeronautics from the California Institute of Technology and BSc and PEng degrees in Mechanical Engineering from Universidad Técnica Federico Santa María in Chile. 
Previous to joining GW, she was Assistant Professor of Mechanical Engineering at Boston University (2008–2013) and Lecturer/Senior Lecturer of Applied Mathematics at University of Bristol, UK (2004–2008). 
Prof. Barba is an Amelia Earhart Fellow of the Zonta Foundation (1999), a recipient of the EPSRC First Grant program (UK, 2007), an NVIDIA Academic Partner award recipient (2011), and a recipient of the NSF Faculty Early CAREER award (2012). 
She was appointed CUDA Fellow by NVIDIA Corporation (2012) and is an internationally recognized leader in computational science and engineering.  
**Headshot**:

**First Name**: Pi-Yueh  
**Last Name**: Chuang  
**Email**: pychuang@gwu.edu  
**Cell Phone**: 202-517-3455  
**Job Title**: PhD student  
**Company**: George Washington University  
**Biography**: 
Pi-Yueh Chuang is a PhD student in Mechanical and Aerospace Engineering at George Washington University, Washington DC. He is a member in Porfessor Lorena A. Barba's research group. 
His current research interests are GPU applications in CFD simulations and immersed boundary methods. 
Prior to his PhD studying, he worked as an engineer in Moldex3D–a company developing mold-flow simulation software–and thought that GPU technologies are the future of industry-oriented CFD software. 
He got his MS degree in Mechanical Engineering from National Taiwan University with thesis and papers focusing on direct simulation Monte Carlo method and nanoscale energy transport. 
He has BS in Power Mechanical Engineering from National Tsing Hua University, Taiwan.  
**Headshot**:  
