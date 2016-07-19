We wrote a wrapper code to bridge PETSc and AmgX libraries to use AmgX's multi-GPU linear solvers in existing PETSc-based CFD codes.
With the wrapper, those codes are able to exploit all available CPU and GPU resources without heavy coding efforts.
The wrapper features a simple usage: the two functions for setting and solving a linear system in the wrapper can directly replace the two in PETSc.
It implicitly carries out data converting/transferring/scattering/gathering and hides all MPI communications.
Benchmarks of real CFD simulations suggest that, with multi-GPU computing, we can save 
1) run times and hardware cost (e.g. a 6-CPU-core workstation with 1 NVIDIA K40c can compete with a 16-node CPU cluster); and
2) cloud HPC cost (e.g. a benchmark on Amazon EC2 shows a 16x cost saving between CPU and GPU clusters)
of scientific simulations.

