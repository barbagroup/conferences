#!/bin/bash

#SBATCH --job-name="PetAmgX-flyingSnake2dRe2000AoA35-atol1e-5-96CPU"
#SBATCH --nodes=8
#SBATCH --ntasks-per-node=12
#SBATCH --time=2-00:00:00
#SBATCH --output=slurm-job-%j.out
#SBATCH --error=slurm-job-%j.err
#SBATCH --partition=allgpu-noecc

source /home/pychuang/moduleLoad.sh
source /home/pychuang/petibm-amgx/envs.sh

export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/c1/apps/cuda/driver/352.63/lib
export PETIBM_DIR=/home/pychuang/petibm-amgx


echo "2D flyingSnake Re2000 96CPU aTol=1e-5 Short Period"

mpiexec -display-map -np 96 ${PETIBM_DIR}/bin/petibm2d -directory /home/pychuang/Cases/flyingSnake/atol_1e-5_short/flyingSnake2dRe2000AoA35_96CPU
