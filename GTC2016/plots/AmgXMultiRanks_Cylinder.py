'''
Whole Cylinder 2D Re40, PCGF + AGG
'''

import numpy
from matplotlib import pyplot

pyplot.style.use('style')

def plotRawCylinder(case, events, timing, plotOrder, figName):
    '''
    '''
    fig = pyplot.figure(figsize=(10, 8), dpi=150)
    ax = fig.gca()

    color_cycle = ax._get_lines.prop_cycler

    bw = 0.5
    bLoc = numpy.arange(1, 4) - 0.25
    bOffSet = numpy.zeros(3)

    for i in plotOrder:

        ax.bar(bLoc, timing[events[i]], bw, label=events[i], bottom=bOffSet, 
                color=next(color_cycle)['color'], lw=0, zorder=0)

        bOffSet += timing[events[i]]


    ax.set_ylabel("Time (min)", fontsize=16)
    ax.set_title("PetIBM + AmgX", fontsize=22)

    ax.set_xlim(0.5, 3.5)
    ax.set_xticks(bLoc+0.25)
    ax.set_xticklabels(case, fontsize=14, fontweight="bold")

    ax.yaxis.grid(zorder=10)

    bars, labels = ax.get_legend_handles_labels()

    pyplot.subplots_adjust(top=0.95, bottom=0.225, left=0.0775, right=0.98)
    pyplot.figlegend(bars, labels, ncol=2,
            loc=8, bbox_to_anchor=[0.525, 0.005], fontsize=15)

    pyplot.savefig(figName)



# first plot
cases = numpy.array(["6 CPU\nonly", "1 CPU\n& 1 GPU", ""])
events = numpy.array(
        ["Initialization", 
         "Preparing Velocity System", 
         "Solving Velocity System", 
         "Preparing Poisson System", 
         "Solving Poisson System", 
         "Projection Step"])
timing = {}
timing[events[0]] = numpy.array(
        [2.3435+7.8894, 7.8249+34.73, 0]) / 60.
timing[events[1]] = numpy.array([25.067, 104.65, 0]) / 60.
timing[events[2]] = numpy.array([30.222, 71.158, 0]) / 60.
timing[events[3]] = numpy.array([1.9671, 4.5373, 0]) / 60.
timing[events[4]] = numpy.array([1838.8, 448.44, 0]) / 60.
timing[events[5]] = numpy.array([2.8628, 6.1477, 0]) / 60.

plotOrder = [4, 2, 3, 1, 5, 0]

plotRawCylinder(cases, events, timing, 
        plotOrder, "rawAmgXMultiRanks_Cylinder2d_1.png")



# second plot
cases = numpy.array(["6 CPU\nonly", "1 CPU\n& 1 GPU", "6 CPU\n& 1 GPU"])

timing = {}
timing[events[0]] = numpy.array(
        [2.3435+7.8894, 7.8249+34.73, 2.2998+12.308]) / 60.
timing[events[1]] = numpy.array([25.067, 104.65, 24.813]) / 60.
timing[events[2]] = numpy.array([30.222, 71.158, 29.792]) / 60.
timing[events[3]] = numpy.array([1.9671, 4.5373, 1.9413]) / 60.
timing[events[4]] = numpy.array([1838.8, 448.44, 1734.3]) / 60.
timing[events[5]] = numpy.array([2.8628, 6.1477, 2.6366]) / 60.

plotRawCylinder(cases, events, timing, 
        plotOrder, "rawAmgXMultiRanks_Cylinder2d_2.png")


# after using wrapper
case = numpy.array(["6 CPU\nonly", "1 CPU\n& 1 GPU", "6 CPU\n& 1 GPU"])

timing = {}
timing[events[0]] = numpy.array(
        [2.3435+7.8894, 7.8249+34.73, 2.1456+10.547]) / 60.
timing[events[1]] = numpy.array([25.067, 104.65, 23.305]) / 60.
timing[events[2]] = numpy.array([30.222, 71.158, 28.017]) / 60.
timing[events[3]] = numpy.array([1.9671, 4.5373, 1.9224]) / 60.
timing[events[4]] = numpy.array([1838.8, 448.44, 464.99]) / 60.
timing[events[5]] = numpy.array([2.8628, 6.1477, 2.6272]) / 60.

plotRawCylinder(cases, events, timing, 
        plotOrder, "newAmgXMultiRanks_Cylinder2d_2.png")

