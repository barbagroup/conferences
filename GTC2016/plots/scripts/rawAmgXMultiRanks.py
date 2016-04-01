import numpy
from matplotlib import pyplot
from matplotlib import gridspec

pyplot.style.use('style')

def plotRawAmgXMultiRanks(nRanks, solveTime, titles, figName):

    fig = pyplot.figure(figsize=(8, 5), dpi=150)
    gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1])

    bw = 0.5
    bLoc = numpy.arange(1, 7) - 0.25

    for i in range(2):
        ax = pyplot.subplot(gs[i])

        ax.bar(bLoc, solveTime[i], bw, 
                label="Solve Time", lw=0, color='#348ABD', zorder=0)


        ax.set_title(titles[i], fontsize=18, 
                fontweight="medium", fontstyle="italic")

        ax.set_ylabel("Time (sec)", fontsize=16)
        ax.tick_params(axis="y", labelsize="14")
        ax.yaxis.grid(zorder=0)

        ax.set_xlabel("Number of MPI processes", fontsize=16)
        ax.set_xlim(0, 7)
        ax.set_xticks(bLoc+0.25)
        ax.set_xticklabels(nRanks[i], fontsize=14)

        bars, labels = ax.get_legend_handles_labels()


    fig.suptitle("Solve Time v.s. Number of MPI Processes", 
            fontsize=22, fontweight="medium", y=0.975)

    pyplot.subplots_adjust(
            top=0.825, bottom=0.1, left=0.083, right=0.99, wspace=0.25)

    pyplot.savefig(figName)



'''
Cylinder 2D Re40, 2.25M, Aggregation, PCGF + Aggregation, on Theo, 1 or 2 K40c
'''

nRanks = [numpy.arange(6)+1, 2*(numpy.arange(6)+1)]
solveTime = [
        numpy.array(
            [1.645976, 3.620308, 5.157521, 6.927330, 8.404358, 13.503613]),
        numpy.array(
            [1.443363, 3.557487, 6.956636, 9.880469, 12.499419, 16.463862])]

titles = ["1 GPU (K40c)", "2 GPU (K40c)"]

figName = "rawAmgXMultiRanks_Aggregation.png"

plotRawAmgXMultiRanks(nRanks, solveTime, titles, figName)


'''
Nx 200 Ny 200 Nz 150, PCGF + Classical, on Theo, 1 or 2 K40c
'''

solveTime = [
        numpy.array(
            [1.340154, 1.981376, 2.304225, 2.596131, 2.364931, 3.258457]),
        numpy.array(
            [0.908612, 1.333168, 1.649151, 2.324669, 2.456639, 3.572393])]

figName = "rawAmgXMultiRanks_Classical.png"

plotRawAmgXMultiRanks(nRanks, solveTime, titles, figName)
