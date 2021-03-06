'''
Nx = 10000, Ny = 10000, 2D Poisson Benchamrks
'''

import numpy
from matplotlib import pyplot

pyplot.style.use('style')

nCPU = numpy.array([16, 32, 64, 128])
Hypre = numpy.array([27.125073, 15.487189, 7.924572, 4.094746])

nGPU = numpy.array([32])
AmgX = numpy.array([1.538988])

#nTheo = numpy.array([])
#AmgXTheo = numpy.array([])


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


# Hypre
bLoc = numpy.arange(start, nCPU.size+start) - 0.25

ax.bar(bLoc, Hypre, bw, label="Hypre BoomerAMG (Intel E5-2670)",
        color=next(color_cycle)['color'], lw=0, zorder=0)

## speed up text
for i in range(nCPU.size):
    ax.annotate(str(numpy.around(Hypre[0]/Hypre[i], 1))+"x", 
            xy=(bLoc[i], Hypre[i]),
            xytext=(bLoc[i], Hypre[i]+0.5),
            fontsize=18, weight="bold", color="red")

start += (nCPU.size+1)
tickLoc += list(bLoc+0.5)
tickLabel += [str(i)+" CPU" for i in nCPU]


# AmgX / ColonialOne
bLoc = numpy.arange(start, nGPU.size+start) - 0.25

ax.bar(bLoc, AmgX, bw, label="AmgX Classical AMG (NVIDIA K20)",
        color=next(color_cycle)['color'], lw=0, zorder=0)

## speed up text
for i in range(nGPU.size):
    ax.annotate(str(numpy.around(Hypre[0]/AmgX[i], 1))+"x", 
            xy=(bLoc[i], AmgX[i]),
            xytext=(bLoc[i], AmgX[i]+0.5),
            fontsize=18, weight="bold", color="red")

start += (nGPU.size+1)
tickLoc += list(bLoc+0.5)
tickLabel += [str(i)+" GPU" for i in nGPU]


# AmgX / Theo(K40c)
#bLoc = numpy.arange(start, nTheo.size+start) - 0.25
#
#ax.bar(bLoc, AmgXTheo, bw, label="AmgX Classical AMG (Workstation)",
#        color=next(color_cycle)['color'], lw=0, zorder=0)
#
#start += (nTheo.size+1)
#tickLoc += list(bLoc+0.5)
#tickLabel += [str(i)+" GPU" for i in nTheo]



# config the figure
ax.set_title("2D Poisson, 100M Unknowns", fontsize=22)

#ax.set_ylim(0, 45)
ax.set_ylabel("Time (sec)", fontsize=20)
ax.yaxis.grid(zorder=0)

ax.set_xlim(0, start-1)
ax.set_xticks(tickLoc)
ax.set_xticklabels(tickLabel, fontsize=16, rotation=315)

bars, labels = ax.get_legend_handles_labels()
ax.legend(bars, labels, loc=0, ncol=1, fontsize=16)


pyplot.tight_layout()
pyplot.savefig("Poisson_N100M2D.png")

