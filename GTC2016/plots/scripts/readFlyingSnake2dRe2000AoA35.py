# coding: utf-8

'''
read performance results of flying snake, 2d, Re2000, AoA35
'''

import os
from matplotlib import pyplot
from matplotlib import gridspec
from parsePetIBMperformance import *


def plotSpeedUpFig(timing, events, cases, xticks, title, 
        plotOrder, subplotOrder, minT, figName):
    '''
    '''

    # plot
    fig = pyplot.figure(figsize=(12, 8), dpi=150)
    gs = gridspec.GridSpec(1, 3, width_ratios=[2, 2, 1])

    for i, subplotCase in enumerate(subplotOrder):

        ax = pyplot.subplot(gs[i])

        color_cycle = ax._get_lines.prop_cycler

        bw = 0.5
        bLoc = {name: i+0.75 for i, name in enumerate(cases[subplotCase])}
        bOffSet = {name: 0 for i, name in enumerate(cases[subplotCase])}

        for order in plotOrder:

            c = next(color_cycle)['color']

            for case in cases[subplotCase]:

                ax.bar(bLoc[case], timing[subplotCase][case][events[order]], 
                        bw, label=events[order], bottom=bOffSet[case], 
                        color=c, lw=0, zorder=10)

                bOffSet[case] += timing[subplotCase][case][events[order]]

        for case in cases[subplotCase]:
            ax.annotate(
                    str(round( minT / timing[subplotCase][case]["total"], 1))+"x", 
                    xy=(bLoc[case], timing[subplotCase][case]["total"]),
                    xytext=(bLoc[case], 
                        timing[subplotCase][case]["total"]+max(bOffSet.values())*0.01),
                    fontsize=18, weight="bold", color="red")



        ax.set_title("Using " + title[subplotCase], fontsize=16, fontweight="bold")

        ax.set_ylim(0, max(bOffSet.values()) * 1.1)
        ax.set_ylabel("Time (hour)", fontsize=16, fontweight="bold")
        ax.tick_params(axis="y", labelsize="16")
        ax.yaxis.grid(zorder=0)

        ax.set_xlim(0.5, len(bLoc)+0.5)
        ax.set_xticks(range(1, len(bLoc)+1))
        ax.set_xticklabels(xticks[subplotCase], fontsize=16, rotation=345, ha="left")


        bars, labels = ax.get_legend_handles_labels()



    fig.suptitle("Flying Snake, 2D, Re=2000, AoA=35", 
            fontsize=24, fontweight="bold", y=0.95)


    pyplot.figlegend(bars[0::len(bLoc)], labels[0::len(bLoc)], ncol=3, 
            loc=8, bbox_to_anchor=[0.5, 0.015],
            fontsize=14)

    pyplot.subplots_adjust(top=0.85, bottom=0.2, left=0.08, right=0.96, wspace=0.3)
    pyplot.savefig(figName, figsize=(10, 8), dpi=150)




def plotAmazonFig(timing, events, cases, xticks, title, plotOrder, minT, figName):
    '''
    '''

    # plot
    fig = pyplot.figure(figsize=(10, 8), dpi=150)
    ax = fig.gca()

    color_cycle = ax._get_lines.prop_cycler

    bw = 0.5
    bLoc = {name: i+0.75 for i, name in enumerate(
    bOffSet = numpy.zeros(case.size)

    for order in plotOrder:

        ax.bar(bLoc, timing[events[order]], bw, 
            label=events[order], bottom=bOffSet, 
            color=next(color_cycle)['color'], lw=0, zorder=10)

        bOffSet += timing[events[order]]

    for i in range(case.size):
        ax.annotate(
                str(numpy.around(
                    timing["total"][0] /
                    timing["total"][i], 1))+"x", 
                xy=(bLoc[i]+0.25, timing["total"][i]),
                xytext=(bLoc[i]+0.125, 
                    timing["total"][i]+timing["total"].max()*0.01),
                fontsize=22, weight="bold", color="red")



    ax.set_title("Flying Snake On Amazon EC2", fontsize=24, fontweight="bold")

    ax.set_ylim(0, timing["total"].max() * 1.1)
    ax.set_ylabel("Time (hour)", fontsize=18, fontweight="bold")
    ax.tick_params(axis="y", labelsize="18")
    ax.yaxis.grid(zorder=0)

    ax.set_xlim(0.5, bLoc[-1]+0.75)
    ax.set_xticks(bLoc+0.25)
    ax.set_xticklabels(case, fontsize=20, fontweight="bold")


    bars, labels = ax.get_legend_handles_labels()


    ax.legend(bars, labels, loc=1, borderaxespad=0, fontsize=16)

    pyplot.savefig(figName, figsize=(10, 8), dpi=150)


def plotFlyingSnakeFigs(filePath, figPath, save):
    '''
    Plot the figures for cylinder flow tests.
    '''

    assert save in [True, False], \
            "Use True or False to specify whether to " +\
            "save the figure or show the figure on screen"

    timing, events = parseResultFiles(filePath, "h")

    keyword = "flyingSnake2dRe2000AoA35_"

    cases = {
            "Amazon": [keyword+"4GPU",keyword+"96CPU"],
            "CPUclusters": [keyword+"12CPU", keyword+"24CPU", 
                            keyword+"48CPU", keyword+"96CPU"],
            "GPUclusters": [keyword+"2GPU", keyword+"4GPU", 
                            keyword+"8GPU", keyword+"16GPU"],
            "workstation": [keyword+"1GPU", keyword+"2GPU"]}

    xticks = {
            "Amazon": ["8 CPU nodes","1 GPU node"],
            "CPUclusters": ["1 CPU node", "2 CPU nodes", "4 CPU nodes", "8 CPU nodes"],
            "GPUclusters": ["1 GPU node", "1 GPU nodes", "1 GPU nodes", "8 GPU nodes"],
            "workstation": ["1 K40c", "2 K40c"]}

    title = {
            "Amazon": "Amazon EC2",
            "CPUclusters": "CPU Clusters",
            "GPUclusters": "GPU Clusters",
            "workstation": "Workstation"}

    plotOrder = [4, 2, 3, 1, 5, 0]
    subplotOrder = ["CPUclusters", "GPUclusters", "workstation"]

    plotSpeedUpFig(timing, events, cases, xticks, title, plotOrder, subplotOrder, 
            timing["CPUclusters"][keyword+"12CPU"]["total"], 
            figPath+"flyingSnake.png")

