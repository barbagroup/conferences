# Using AmgX to accelerate a PETSc-based Immersed-Boundary Method code

_Olivier Mesnard, Pi-Yueh Chuang, and Lorena A. Barba_

_The George Washington University_

_29th International Conference on Parallel Computational Fluid Dynamics; May 15-17, 2017; Glasgow, Scotland_

## Slide 1: Introduction
Hi!
I am a member of Prof. Barba's research group at the George Washington University working on immersed-boundary methods with application to bio-locomotion.
Today, I am reporting how we painlessly enable GPU computing in one of our research codes using the Nvidia AmgX library.

## Slide 2: PetIBM
This is my second time at Parallel CFD.
Two years ago in Montreal, I presented our new (at that time) research code called PetIBM.
PetIBM solves the 2D and 3D incompressible Navier-Stokes equations using a finite-difference method and a projection approach on distributed-memory architectures.
We use data structures and parallel routines of the open-source library PETSc that is being developed since the early nineties at the Argonne National Lab.
We chose PETSc as it hides a lot of MPI implementations from users.
In PetIBM, we have also implemented an immersed-boundary method to solve external flows around rigid objects.
With this method, we relax the constraint on the mesh to fit to the surface of the object and solve the fluid equations on simple structured Cartesian grids.
The presence of an immersed boundary is taken into account with an additional forcing term in the momentum equation and an extra constraint for the no-slip condition at the interface.
The boundary is represented by a collection of markers and the transfer between the Lagrangian mesh and the background Eulerian grid is handled by regularized delta functions.

## Slide 3: Immersed-Boundary Projection Method
There are a multitude of immersed-boundary methods and in PetIBM, we chose  the immersed-boundary projection method (IBPM) that was introduced by Taira and Colonius in 2007.
The method builds on the work from Perot in the nineties in which the projection method is seen as a block-LU decomposition.
The pressure field can be viewed as a Lagrange multiplier used to enforce the divergence-free condition on the velocity field.
Similarly, the boundary forces can be viewed as Lagrange multipliers to satisfy the no-slip condition at the interface.
In this immersed-boundary method, the pressure field and the boundary forces are grouped together and decoupled from the velocity via a block-LU decomposition.
This way, we retrieve the sequence of operations of the traditional fractional step method: we solve a system for the velocity and project it onto the divergence-free space while enforcing the no-slip condition at the boundary by solving a modified-Poisson system.
By the end of each time step, the two constraints are both satisfied.

## Slide 4: Application to gliding snake
One of our research applications deals with the aerodynamics of a gliding snake that lives in the South-East region of Asia.
The snake jumps from tree branches, expands its rib cage morphing its circular cross-section into a triangular one with the formation of lips.
Three years ago, our group published a 2D numerical investigation of the aerodynamic forces acting on such expanded cross-section.
At that time, we used another code, called cuIBM, that implements the same immersed-boundary method making use of GPU computing on a single device.
Using cuIBM, we observed a spike in the lift curve for Reynolds number above 2000 when the cross-section forms a 35-degree angle of attack with the freestream flow.
Interestingly, this extra upward force has been previously observed experimentally for the same angle of attack.
Despite this matching angle, we know that for those Reynolds numbers, the flow is three-dimensional.
And 3D mesh-grids being larger, with our previous code, we would be rapidly limited by the memory available on a single GPU device.
So, we took a step back from GPU computing to develop PetIBM that runs on multi CPU nodes.

## Slide 5: Modified-Poisson system
With this immersed-boundary method, we solve a modified-Poisson system for the couple pressure/boundary forces.
The bottom-right figure gives you an idea of the non-zero structure of such system.
The top-left part corresponds to the traditional Poisson matrix.
The bottom-left and top-right parts model the interaction between the immersed boundary and the surrounding flow.
In the presence of a body, the matrix becomes larger and contains off-diagonal terms making the system more expensive to solve.
As an example, when we used a conjugate gradient method preconditioned by an aggregation algebraic multigrid technique from the PETSc library on a single node, with 16 CPU cores, solving the modified-Poisson system takes about 90% of the total runtime.
So with PetIBM, our objective was to reduce the time-to-solution for this system by using GPU computing without rewriting too many parts of the code.

## Slide 6: Nvidia AmgX library
We chose the library AmgX that is developed and supported by Nvidia.
AmgX gives you access to various Krylov solvers and different algebraic multigrid techniques with the possibility to solve systems on multiple CUDA-capable GPU devices located on a single node or on multiple nodes.
As of now, AmgX is available with a free license for non-commercial use; you can download the library on their website.
In PetIBM, we want to use AmgX to iteratively solve our Poisson system.
The problem is that PetIBM already heavily relies on the PETSc library which has different data structures than AmgX as they target different hardware.

## Slide 7: AmgXWrapper
Thus, we decided to develop AmgXWrapper, a simple interface between AmgX and PETSc, that handles the data conversion between the two libraries.
We tried to make it simple and not specific to our code PetIBM, so that a user would just have to initialize, set the matrix (with a PETSc object), solve the system at each time step (using PETSc vectors), then finalize to release the memory.
So, for those already using PETSc and interested in GPU computing with AmgX, our wrapper is available on GitHub.

## Slide 8: AmgXWrapper - Poisson system
One issue we had to deal with when developing our wrapper was how to reconcile the PETSc domain decomposition based on the number of MPI processes launched and the AmgX decomposition on GPUs.
The top figure reports the time-to-solution for a Poisson system using our AmgX wrapper, for an increasing number of MPI processes and solving the system on 1 and 2 GPU devices.
The blue bars show our first attempt with the wrapper where the time-to-solution of the Poisson system increases with the number of MPI processes.
This is because we were creating a number of AmgX solver instances equals to the number of PETSc sub-domains.
All the sub-domain solvers would be competing for the GPU resources, increasing the time-to-solution.
We opted for a simple workaround: create extra communicators so that only one MPI process would be responsible for launching an AmgX solver instance.
On each node, we split processes in a number of groups equals to the number of GPUs available.
The PETSc data are gathered onto one master process that is in charge of the data conversion and the transfer between host and device.
The master processes are part of another communicator that gather and scatter data across multiple nodes.
As you see with the red bars, with this workaround in place, the time-to-solution for the Poisson system remains constant as we increase the number of the MPI processes.

## Slide 9: Benchmark snake application
We used our 2D snake application on a mesh-grid with 3M cells to report speedup in PetIBM using AmgX through our wrapper.
In all runs shown in this figure, the modified-Poisson system was solved using a conjugate-gradient method preconditioned by an algebraic multigrid technique with aggregation.
CPU cases shown on the left part were run using PETSc with 12 CPU cores per node.
GPU cases at the center and right parts of the figure were run using AmgX with 12 CPU cores and 2 K20 devices per node.
For CPU runs, we obtained good scaling as we increase the number of nodes but still, we see that the Poisson solver takes most of the runtime.
With GPU computing, we already observed a 21-time speedup when comparing 1 GPU node and 1 CPU node.
We even obtained remarkable speed-up on one of our workstations.
With AmgX and our wrapper, we have been able to considerably reduce the time-to-solution of the Poisson system.
But as said before, because the pressure and the boundary forces are coupled in this projection method, the modified-Poisson system is difficult to solve.
So, we also tried to use a new immersed-boundary technique.

## Slide 10: decoupled immersed-boundary method
We implemented a method proposed by Li and co-workers last year.
The method applies 2 block-LU decompositions instead of one.
The first factorization decouples the forces from the pressure and velocity fields.
The second one decouples the pressure from the velocity.
In the end, we solve a system for a velocity field that is projected on the divergence-free space by solving a classical Poisson system.
After that, a small system for the boundary forces is solved to enforce the no-slip condition.
Thus, the two constraints are not both satisfied by the end of the time step.
So, next, we want to know if using this new method will affect our results for the snake application.

## Slide 11: IBPM vs. decoupled - force coefficients
Here, we report the instantaneous force coefficients generated by the snake cross-section using the immersed-boundary projection method and its decoupled version.
With a modified-Poisson system, we used AmgX with aggregation multigrid.
For the decoupled method, we used AmgX classical multigrid, which is suitable for a pure Poisson system.
The force coefficients (lift on top, drag at the bottom) obtained with the two methods are visually identical.
This means that for our application, it was not necessary to satisfy both constraints simultaneously.

## Slide 12: IBPM vs. decoupled - runtimes
Now, lets have a look at the consequences on the simulation runtime.
The two left bars show the walltimes obtained with the immersed-boundary projection method.
By enabling GPU computing with AmgX, we observe a 2.4-time speedup in our simulation.
More interestingly, with the decoupled method and AmgX, we now report a 6-time speedup and solving the Poisson system iteratively is not anymore the bottleneck in our simulations.

## Slide 13: Microsoft Azure - OSU micro-benchmarks
Most of the simulations reported so far were run on Colonial One, our University HPC cluster that features CPU nodes and GPU nodes with K20 devices.
Having access to this cluster is great, but sometimes maintenance issues slow down your progress.
Waiting in queue for an undefined period of time can also be frustrating.
So, we wanted to look for an alternative to our University cluster.
Last year, we got a Sponsorship from Microsoft Azure for 20,000 CPU hours to be able to run our code on their public cloud platform.
For those who are interested in using cloud computing, here is the website where you can apply for such grant.
To start with, we performed some micro-benchmarks from the Ohio State University to look at the point-to-point bandwidth and latency to compare communication performances between our University cluster and Microsoft Azure A9 instances.
As you see, the CPU node specifications of the two platforms are identical and we report similar results in terms of latency and bandwidth.

## Slide 14: Microsoft Azure - Poisson benchmark
We also ran a Poisson benchmark on a mesh-grid with 46M cells solving the system with a conjugate-gradient method from PETSc preconditioned by a classical multigrid technique from Hypre BoomerAMG.
These results confirms that we are able to get similar performances on a public cloud compared to our local University cluster.

## Slide 15: Microsoft Azure - CPU and GPU Instances
On Azure, you pay-as-you-go and once you are done with your runs you just have to release the resources. No need for you to wait in queue.
Since last year, Microsoft Azure also provides GPU instances with the NC series that features K80 GPUs with up to 4 devices per node.
(Our University cluster only provides two K20s per node.)
Of course, the virtual machines that have GPU capabilities are more expensive than the CPU compute nodes but we hope that using AmgX, we can still lower our cost when running our code.

## Slide 16: Microsoft Azure - 2D snake
We ran our 2D snake simulation using the newly implemented decoupled immersed-boundary method to compare runtimes between a CPU version of PetIBM on a cluster with A9 instances and a GPU version with AmgX on different instances of the NC series.
In terms of runtime, we see that we obtained similar performances on a cluster of 8 A9 nodes and on a single NC6 node (which has 6 CPU cores and 1 K80).
The CPU run cost about $12.5, while the run on the NC6 instance cost only 75 cents.
By enabling GPU computing in our PETSc-based code, we reduced the cost by 95%.

## Slide 17: Microsoft Azure - 3D snake
We realized a similar analysis on a 3D mesh-grid that contains 46M cells.
Here, we see that a cluster with 4 CPU nodes gives us the same runtime than a single NC24 instance (NC24 with 24 CPU cores and 4 K80 GPU devices).
The cost for the CPU run is about $15.5, while the cost for the GPU run is just below $8.
Our 3D test-case on a single GPU compute node cost twice less than the same run on 4 CPU nodes.
Note that, this meshgrid of 46M cells filled almost entirely the memory of the 4 K80 devices.
To run bigger meshes with our code and AmgX, we would need to use more than one node.
We are not showing results on multiple GPU nodes on Azure as there is not yet fast network communication available for those nodes.
Over the last weeks, we have been in touch with Microsoft Azure; they told us that they will very soon release GPU instances with fast-communication network.

## Slide 18: Conclusions
In this talk, I mentioned how we enable GPU computing in our existing PETSc-based code and reduce the time-to-solution of the modified-Poisson system.
For that purpose, we developed a wrapper to interface PETSc and AmgX.
For those interested, you can have a look at it on GitHub.
We also observed speedup in our snake application by using a decoupled version of the immersed-boundary projection method.
Finally, with Microsoft Azure, we started to investigate the possibility of using cloud computing for our CFD simulations.
With AmgX, we saw that we could considerably reduce our cloud computing expenses.
Again I'm spreading the word, you can apply for a Microsoft grant on their website.
