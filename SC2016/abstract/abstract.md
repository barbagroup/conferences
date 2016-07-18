We wrote a wrapper code to bridge PETSc and AmgX libraries in order to utilize AmgX's multi-GPU linear solvers in existing PETSc-based CFD codes.
The wrapper features a simple usage: the two functions for setting matrix and solving system in the wrapper can directly replace the two in PETSc.
It has capability to exploit all available CPU and GPU resources.
All these are accomplished through converting/transfering data implicitly between the two libraries,
hiding MPI communications,
and merging sub-systems without users' knowing.
We performed benchmarks to understand speed-ups after incorporating multi-GPU capability in PETSc applications. 
Results of benchmarks suggest that, with multi-GPU computing, we can save 
1) run times and hardware cost (e.g.\ a 6-CPU-core workstation with 1 NVIDIA K40c can compete with a 16-node CPU cluster); and
2) cloud HPC cost (e.g.\ a benchmark on Amazon EC2 shows a 16x cost saving between CPU and GPU clusters)
of scientific simulations.

