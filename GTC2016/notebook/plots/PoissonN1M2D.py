'''
Nx = 1000, Ny = 1000, 2D Poisson Benchamrks
'''

import numpy
from matplotlib import pyplot

pyplot.style.use('style')

nCPU = numpy.array([16, 32, 64, 128])
Hypre = numpy.array([0.24964, 0.118576, 0.078802, 0.065847])
GAMG = numpy.array([0.55063, 0.231961, 0.106224, 0.064558])

nGPU = numpy.array([1, 2, 4, 8, 16, 32])
AmgX = numpy.array([0.143489, 0.132337, 0.116464, 0.118274, 0.153426, 0.269259])

nTheo = numpy.array([1, 2])
AmgXTheo = numpy.array([0.128786, 0.120883])


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
ax.set_title("2D Poisson, 1M Unknowns", fontsize=22)

#ax.set_ylim(0, 45)
ax.set_ylabel("Time (sec)", fontsize=20)
ax.yaxis.grid(zorder=0)

ax.set_xlim(0, start-1)
ax.set_xticks(tickLoc)
ax.set_xticklabels(tickLabel, fontsize=16, rotation=315)

bars, labels = ax.get_legend_handles_labels()
ax.legend(bars, labels, loc=0, ncol=1, fontsize=16)


pyplot.tight_layout()
pyplot.savefig("Poisson_N1M2D.png")

