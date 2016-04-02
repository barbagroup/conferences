import numpy
from matplotlib import pyplot
from matplotlib import gridspec

pyplot.style.use('style')

def plotNewAmgXMultiRanks(nRanks, solveTime, titles, figName, ylim=None):

    fig = pyplot.figure(figsize=(8, 5), dpi=150)
    gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1])

    for i in range(2):

        ax = pyplot.subplot(gs[i])

        bw = 0.35
        bLoc = numpy.arange(1, 7) - 0.35

        ax.bar(bLoc, solveTime['raw'][i], bw, 
                label="Solve Time w/o wrapper", lw=0, color='#348ABD', zorder=0)

        bLoc += 0.35

        ax.bar(bLoc, solveTime['new'][i], bw, 
                label="Solve Time w/ wrapper", lw=0, color='#A60628', zorder=0)


        ax.set_title(titles[i], fontsize=18, 
                fontweight="medium", fontstyle="italic")

        ax.set_ylabel("Time (sec)", fontsize=16)
        if ylim != None and type(ylim) == list:
            ax.set_ylim(ylim)
        ax.tick_params(axis="y", labelsize="14")
        ax.yaxis.grid(zorder=0)

        ax.set_xlabel("Number of MPI processes", fontsize=16)
        ax.set_xlim(0, 7)
        ax.set_xticks(bLoc)
        ax.set_xticklabels(nRanks[i], fontsize=14)

        bars, labels = ax.get_legend_handles_labels()


    fig.suptitle("Solve Time v.s. Number of MPI Processes", 
            fontsize=22, fontweight="medium", y=0.975)

    pyplot.figlegend(bars, labels, ncol=2, 
            loc=8, bbox_to_anchor=[0.53, 0.015],
            fontsize=14)

    pyplot.subplots_adjust(
            top=0.825, bottom=0.225, left=0.083, right=0.99, wspace=0.25)

    pyplot.savefig(figName)



'''
Cylinder 2D Re40, 2.25M, Aggregation, PCGF + Aggregation, on Theo, 1 or 2 K40c
'''

nRanks = [numpy.arange(6)+1, 2*(numpy.arange(6)+1)]
solveTime = {
        'raw': [numpy.array([1.645976, 3.620308, 
                    5.157521, 6.927330, 8.404358, 13.503613]), 
                numpy.array([1.443363, 3.557487, 
                    6.956636, 9.880469, 12.499419, 16.463862])],
        'new': [numpy.array([1.645149, 1.654546,
                    1.652971, 1.658068, 1.657542, 1.662599]), 
                numpy.array([1.444257, 1.456718,
                    1.463075, 1.492746, 1.543774, 1.583597])]}

titles = ["1 GPU (K40c)", "2 GPU (K40c)"]

figName = "../newAmgXMultiRanks_Aggregation.png"

plotNewAmgXMultiRanks(nRanks, solveTime, titles, figName, [0, 18])


'''
Nx 200 Ny 200 Nz 150, PCGF + Classical, on Theo, 1 or 2 K40c
'''

solveTime = {
        'raw': [numpy.array([1.340154, 1.981376, 
                    2.304225, 2.596131, 2.364931, 3.258457]),
                numpy.array([0.908612, 1.333168, 
                    1.649151, 2.324669, 2.456639, 3.572393])],
        'new': [numpy.array([1.339127, 1.349229,
                    1.341093, 1.307963, 1.305384, 1.307264]), 
                numpy.array([0.908919, 0.906064,
                    0.904388, 1.149481, 0.915134, 1.225759])]}


figName = "../newAmgXMultiRanks_Classical.png"

plotNewAmgXMultiRanks(nRanks, solveTime, titles, figName, [0, 4])
