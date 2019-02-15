Abstract
========

## Title

High-fidelity overland hydrocarbon HCA analysis with GeoClaw and cloud computing

## Short summary

## Abstract

Title 49 CFR §195.452 requires overland hydrocarbon flow analysis for hazardous liquid pipelines in High Consequence Area (HCA). 
Open-source numerical solvers for high-fidelity HCA analysis, however, are not widely available nor used in the risk assessment community. 
A significant reason is a high demand for computing power due to the complexity of modeling. 
When it comes to HCA analysis, a pipeline segment may contain tens or hundreds of potential rupture points that requires analysis. 
Therefore the mainstream of HCA analysis nowadays still models the overland hydrocarbon flow with 1D kinematic-wave approximation to speed-up the analysis, though the analysis results usually deviate from reality. 
Given the advance in cloud computing, we believe the HCA analysis should now move on to a more sophisticated model and exploit the power of cloud computing. 
In this work, we present new GeoClaw development that serves such purpose and a Python workflow for Microsoft Azure.

GeoClaw, initially designed for tsunami simulations, solves 2D full shallow-water equations (SWE) on complex topography and is under a public license (BSD 3-Clause). 
GeoClaw utilizes OpenMP parallelization and adaptive mesh refinement (AMR) techniques to accelerate simulations. 
To perform HCA analysis with GeoClaw, we expand GeoClaw's capabilities with the Darcy-Weisbach friction models, in-land hydrological features, evaporation models, and the capability of handling pipeline rupture points. 
While the core code of GeoClaw is in Fortran, we wrap the modified GeoClaw solver with a Python calling interface. 
The Python interface controls the simulation workflow on a local machine. 
It automatically downloads topography rasters and hydrological features from USGS (United States Geological Survey) REST endpoints, converts input data, and then performs post-processing.

The modified GeoClaw and the Python calling interface are then together packaged into a Docker image. 
We further use Python to deploy the Docker containers to Microsoft Azure clusters. 
With the Python tools, we can create Microsoft Azure clusters and resources specific to GeoClaw's needs and submit simulations to cloud clusters from local machines. 
The tools can monitor the clusters and simulations. 
Auto-resizing of the clusters and auto-downloading of the completed cases happen during the monitoring. 
Once the tasks in the task scheduler are all done, the Python tools delete all cloud resources. 
The whole workflow is designed for the use case when there are a bunch of potential rupture points along a pipeline segment.

We additionally develop a Python toolbox for ArcGIS Pro. 
The Python toolbox provides not only an interface to GeoCalw but also an interface to Microsoft Azure. 
ArcGIS users can prepare simulation cases and interact with Azure in ArcGIS Pro. 
Alternatively, for non-ArcGIS users, Jupyter Notebook can carry out the same workflow and also serves as auto-generated reports.

In this presentation, we will introduce the modifications we made in GeoClaw and the concept of our Microsoft Azure workflow. 
We will also share some technical problems encountered during the development so that audiences can save time when having similar issues in the future. 
Showcases include the usage of the GUI of ArcGIS Pro Python toolbox, Jupyter Notebook adaptation, and some simulation results.

## Complementary data

1. GeoClaw, http://www.clawpack.org/geoclaw.html
2. GeoClaw for overland simulation, https://github.com/barbagroup/geoclaw
3. geoclaw-landspill-cases, https://github.com/barbagroup/geoclaw-landspill-cases
4. geoclaw-azure-launcher, https://github.com/barbagroup/geoclaw-azure-launcher

