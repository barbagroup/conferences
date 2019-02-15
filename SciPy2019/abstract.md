Abstract
========

## Title

Python workflow for high-fidelity modeling of overland hydrocarbon flows with GeoClaw and cloud computing

## Short summary

We expanded GeoClaw, a shallow-water solver, for computing overland hydrocarbon flows, and developed a Python workflow for risk analysis of pipeline ruptures on Microsoft Azure cloud resources.
The added functionality on GeoClaw includes rupture-point inflows, evaporation, Darcy-Weisbach friction, and in-land hydrologic features.
The Python workflow automates running and controlling simulations on Azure clusters.
The goal is performing analysis on hundreds or thousands of potential rupture points along a pipeline.
We also developed a Python toolbox that integrates GeoClaw and the Azure workflow with ArcGIS Pro,
and an equivalent Jupyter-based workflow, while Jupyter notebooks also serve as automatic reports.

## Abstract

Pipeline operators are required by law to assess the risk of pipe ruptures over areas where spills of hazardous liquids can have consequences to health and safety or the environment.
Current analysis methods for overland hydrocarbon flow represent the flow with 1D kinematic-wave approximation, even though the analysis results usually deviate from reality, due to cost constraints.
Pipeline segments may contain tens or hundreds of potential rupture points that require analysis.  
Thus, high-fidelity analysis is not used in the risk-assessment community because of both modeling complexity and the high computing power it demands. 
Given recent advances in cloud computing, we believe this type of analysis could now move on to more sophisticated modeling and exploit the power of cloud nodes. 
Open-source numerical solvers for this type of analysis are not available or have not been adapted to this application. 
In this work, we present new developments built on the open-source GeoClaw software for high-fidelity modeling of overland hydrocarbon flows, and a Python workflow for running the analysis on Microsoft Azure nodes.

GeoClaw, initially designed for tsunami simulations, solves the 2D full shallow-water equations (SWE) on complex topography and is under a public license (BSD 3-Clause). 
It is parallelized with OpenMP and uses adaptive mesh refinement (AMR) techniques to accelerate the simulations. 
We expanded GeoClaw's capabilities to use it for overland flow of hydrocarbons, adding Darcy-Weisbach friction models, in-land hydrological features, evaporation models, and the capability of handling pipeline rupture points. 
As the core of GeoClaw is written in Fortran, we wrapped the modified GeoClaw solver with a Python calling interface. 
This interface is used to control the simulation workflow on a local machine. 
It automatically downloads topography rasters and hydrological features from USGS (United States Geological Survey) REST endpoints, converts input data, and also performs post-processing of the results.

The modified GeoClaw software and the new Python calling interface were packaged into a Docker image. 
We further use Python to deploy the Docker containers to Microsoft Azure clusters. 
With the Python tools, we can create Microsoft Azure clusters and resources specific to GeoClaw's needs and submit simulations to cloud clusters from local machines. 
The tools can also monitor the clusters and simulations. 
Auto-resizing of the clusters and auto-downloading of the completed cases happen during the monitoring. 
Once the tasks in the task scheduler are all complete, the Python tools delete all cloud resources. 
The whole workflow is designed for the use case when there are many potential rupture points along a pipeline segment.

Additionally, we developed a Python toolbox for ArcGIS Pro. 
The Python toolbox provides not only an interface to GeoClaw but also an interface to Microsoft Azure. 
ArcGIS users can prepare simulation cases and interact with Azure in ArcGIS Pro. 
Alternatively, for non-ArcGIS users, we have an equivalent workflow using Jupyter that also auto-generates reports as Jupyter notebooks.

In this presentation, we will describe the modifications we made to the GeoClaw software and the concept of our Microsoft Azure workflow. 
We will also share some technical problems encountered during the development so that audiences can save time when having similar issues in the future. 
The talk will also showcase the usage of the GUI of ArcGIS Pro Python toolbox, Jupyter Notebook adaptation, and model simulation results.

## Complementary data

1. GeoClaw, http://www.clawpack.org/geoclaw.html
2. GeoClaw for overland simulation, https://github.com/barbagroup/geoclaw
3. geoclaw-landspill-cases, https://github.com/barbagroup/geoclaw-landspill-cases
4. geoclaw-azure-launcher, https://github.com/barbagroup/geoclaw-azure-launcher

