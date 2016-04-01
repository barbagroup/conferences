'''
Nx = 100, Ny = 100, Nz = 100, 3D Poisson Benchamrks
'''

import numpy
from matplotlib import pyplot

pyplot.style.use('style')

nCPU = numpy.array([16, 32, 64, 128])
Hypre = numpy.array([0.424199, 0.235875, 0.298645, 0.439293])
GAMG = numpy.array([0.56808, 0.265202, 0.122213, 0.104126])

nGPU = numpy.array([1, 2, 4, 8, 16, 32])
AmgX = numpy.array([0.223277, 0.185389, 0.125234, 0.129827, 0.146559, 0.169065])

nTheo = numpy.array([1, 2])
AmgXTheo = numpy.array([0.193998, 0.167075])


# ===========================
# plot
# ===========================

fig = pyplot.figure(figsize=(10, 5))
ax = fig.gca()
color_cycle = ax._get_lines.prop_cycler

start = 1
tickLoc = []
tickLabel = []
bw = 0.5


# GAMG & Hypre
bLoc = numpy.linspace(start, nCPU.size+1.5, nCPU.size) - 0.25
ax.bar(bLoc, GAMG, bw, label="PETSc GAMG (Intel E5-2670)",
        color=next(color_cycle)['color'], lw=0, zorder=0)

bLoc += 0.5
ax.bar(bLoc, Hypre, bw, label="Hypre BoomerAMG (Intel E5-2670)",
        color=next(color_cycle)['color'], lw=0, zorder=0)

tickLoc += list(bLoc+0.3)
tickLabel += [str(i)+" CPU" for i in nCPU]

start += (nCPU.size*2)


# AmgX / ColonialOne
bLoc = numpy.arange(start, nGPU.size+start) - 0.25

ax.bar(bLoc, AmgX, bw, label="AmgX Classical AMG (NVIDIA K20)",
        color=next(color_cycle)['color'], lw=0, zorder=0)

start += (nGPU.size + 1)
tickLoc += list(bLoc+0.5)
tickLabel += [str(i)+" GPU" for i in nGPU]


# AmgX / Theo(K40c)
bLoc = numpy.arange(start, nTheo.size+start) - 0.25

ax.bar(bLoc, AmgXTheo, bw, label="AmgX Classical AMG (NVIDIA K40c)",
        color=next(color_cycle)['color'], lw=0, zorder=0)

start += (nTheo.size + 1)
tickLoc += list(bLoc+0.5)
tickLabel += [str(i)+" GPU" for i in nTheo]


# config the figure
ax.set_title("3D Poisson, 1M Unknowns", fontsize=22)

#ax.set_ylim(0, 0.8)
ax.set_ylabel("Time (sec)", fontsize=20)
ax.yaxis.grid(zorder=0)

ax.set_xlim(0, start-1)
ax.set_xticks(tickLoc)
ax.set_xticklabels(tickLabel, fontsize=16, rotation=315)

bars, labels = ax.get_legend_handles_labels()
ax.legend(bars, labels, loc=0, ncol=1, fontsize=16)


pyplot.tight_layout()
pyplot.savefig("Poisson_N1M3D.png")

