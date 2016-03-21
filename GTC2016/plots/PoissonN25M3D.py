'''
Nx = 500, Ny = 250, Nz = 200, 3D Poisson Benchamrks
'''

import numpy
from matplotlib import pyplot

pyplot.style.use('style')

nCPU = numpy.array([16, 32, 64, 128])
Hypre = numpy.array([16.084, 7.552423, 4.350115, 2.368264])

nGPU = numpy.array([8, 16, 32])
AmgX = numpy.array([1.185639, 0.865481, 0.555222])

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
            xytext=(bLoc[i]-0.1, Hypre[i]+0.15),
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
            xytext=(bLoc[i]-0.1, AmgX[i]+0.15),
            fontsize=18, weight="bold", color="red")

start += (nGPU.size+1)
tickLoc += list(bLoc+0.5)
tickLabel += [str(i)+" GPU" for i in nGPU]


# AmgX / Theo(K40c)
#bLoc = numpy.arange(start, nTheo.size+start) - 0.25
#
#ax.bar(bLoc, AmgXTheo, bw, label="AmgX Classical AMG (NVIDIA K40c)",
#        color=next(color_cycle)['color'], lw=0, zorder=0)
#
## speed up text
#for i in range(nTheo.size):
#    ax.annotate(str(numpy.around(Hypre[0]/AmgXTheo[i], 1))+"x", 
#            xy=(bLoc[i], AmgXTheo[i]),
#            xytext=(bLoc[i]-0.1, AmgXTheo[i]+0.15),
#            fontsize=18, weight="bold", color="red")

#start += (nTheo.size+1)
#tickLoc += list(bLoc+0.5)
#tickLabel += [str(i)+" GPU" for i in nTheo]


# config the figure
ax.set_title("3D Poisson, 25M Unknowns", fontsize=22)

#ax.set_ylim(0, 45)
ax.set_ylabel("Time (sec)", fontsize=20)
ax.yaxis.grid(zorder=0)

ax.set_xlim(0, start-1)
ax.set_xticks(tickLoc)
ax.set_xticklabels(tickLabel, fontsize=16, rotation=315)

bars, labels = ax.get_legend_handles_labels()
ax.legend(bars, labels, loc=0, ncol=1, fontsize=16)


pyplot.tight_layout()
pyplot.savefig("Poisson_N25M3D.png")

