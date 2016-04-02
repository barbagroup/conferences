# coding: utf-8

'''
read performance results of 2D cylinder flow, Re40
'''

import os
from matplotlib import pyplot
from parsePetIBMperformance import *

def plotOneCylinderFig(
        caseNames, caseNameDict, events, timing, plotOrder, figName, save):
    '''
    Plot the figures for cylinder flow tests.
    '''

    assert save in [True, False], \
            "Use True or False to specify whether to " +\
            "save the figure or show the figure on screen"

    fig = pyplot.figure(figsize=(10, 8), dpi=150)
    ax = fig.gca()

    color_cycle = ax._get_lines.prop_cycler

    bw = 0.5
    bLoc = {caseName: i+0.75 for i, caseName in enumerate(caseNames)}
    bOffSet = {caseName: 0 for i, caseName in enumerate(caseNames)}

    xticks = [caseNameDict[name] for name in caseNames]

    for i in plotOrder:

        c = next(color_cycle)['color']

        for caseName in caseNames:

            ax.bar(bLoc[caseName], timing[caseName][events[i]], bw, 
                    label=events[i], bottom=bOffSet[caseName], 
                    color=c, lw=0, zorder=0)

            bOffSet[caseName] += timing[caseName][events[i]]


    ax.set_ylabel("Time (min)", fontsize=16)
    ax.set_title("PetIBM + AmgX", fontsize=22)

    ax.set_xlim(0.5, 3.5)
    ax.set_xticks(range(1, 4))
    ax.set_xticklabels(xticks, fontsize=14, fontweight="bold")

    ax.yaxis.grid(zorder=10)

    bars, labels = ax.get_legend_handles_labels()

    pyplot.subplots_adjust(top=0.95, bottom=0.225, left=0.0775, right=0.98)
    pyplot.figlegend(bars[0::len(caseNames)], labels[0::len(caseNames)], ncol=2,
            loc=8, bbox_to_anchor=[0.525, 0.005], fontsize=15)

    if save:
        pyplot.savefig(figName)
    else:
        pyplot.show()


def plotCylinderFigs(folder, saveDir, save):
    '''
    Plot all figures for 2D cylinder flow (Re=40) for GTC presentation
    '''

    assert save in [True, False], \
            "Use True or False to specify whether to " +\
            "save the figure or show the figure on screen"

    data, events = parseResultFiles(folder, "m")

    caseNameDict = {
            "pure6CPU": "6 CPU\nonly",
            "6CPU1GPU_Consolidation": "6 CPU\n&1 GPU",
            "6CPU1GPU_noConsolidation": "6 CPU\n&1 GPU",
            "1CPU1GPU": "1CPU\n&1 GPU"}

    cases = [["pure6CPU", "1CPU1GPU"], 
             ["pure6CPU", "1CPU1GPU", "6CPU1GPU_noConsolidation"], 
             ["pure6CPU", "1CPU1GPU", "6CPU1GPU_Consolidation"]]

    plotOrder = [4, 2, 3, 1, 5, 0]

    figNames = [
            saveDir + "/rawAmgXMultiRanks_Cylinder2d_1.png", 
            saveDir + "/rawAmgXMultiRanks_Cylinder2d_2.png", 
            saveDir + "/newAmgXMultiRanks_Cylinder2d.png"]
    
    for i in range(len(cases)):
        plotOneCylinderFig(
            cases[i], caseNameDict, events, data, plotOrder, figNames[i], save)

