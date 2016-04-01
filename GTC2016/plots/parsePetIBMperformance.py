# coding: utf-8

'''
Functions for parsing performance files from PetIBM
'''

import os
import re
import numpy
from matplotlib import pyplot
from matplotlib import gridspec

pyplot.style.use('style')


class NoInfoError(Exception):
    '''
    An error handler for errors occurs during parsing performance files.
    '''
    def __init__(self, _value="No info found!"):
        '''
        '''
        self.value = _value

    def __str__(self):
        '''
        '''
        return repr(self.value)



def findResultFiles(resultPath):
    '''
    Get the full path of each performance files under a given directory.
    '''

    resultFiles = []

    for root, dirs, files in os.walk(resultPath):
        for f in files:
            if f == "performanceSummary.txt":
                resultFiles.append(root + "/" + f)

    return resultFiles


def getCaseName(content):
    '''
    Obtain the case name (the name of the folder containing 
    performanceSummary.txt).
    '''

    print(content)

    key = re.compile(".*?" + "/(?P<case>[^/]*)/" + "performanceSummary.txt")
    match = key.search(content)

    return match.groupdict()["case"]


def parseSingleResultFile(perfFile, unit):
    '''
    Parse a single performanceSummary.txt.
    '''

    uConvert = {"s": 1., "m": 60., "h": 3600.}

    assert unit in uConvert.keys(), \
            "The unit of timing should be one of " +\
            "'s' (second), 'm' (minute), or 'h' (hour)!"


    print("parsing the case name of " + perfFile + " ...")
    
    caseName = getCaseName(perfFile)

    print("opening " + perfFile + " ...")

    f = open(perfFile, "r", encoding="utf-8", errors="replace")
    content = f.read()
    f.close()

    print("parsing " + perfFile + " ...")

    caseInfoKey = \
        re.compile(
                "Time\ \(sec\):\s*" + "(?P<total>\S*)" +
                ".*?" + 
                "Main\ Stage:\ " + "(?P<main>\S*)" + ".*?" +
                "initialize:\ " + "(?P<init>\S*)" + ".*?" +
                "RHSVelocity:\ " + "(?P<rhsV>\S*)" + ".*?" +
                "solveVelocity:\ " + "(?P<solveV>\S*)" + ".*?" +
                "RHSPoisson:\ " + "(?P<rhsP>\S*)" + ".*?" +
                "solvePoisson:\ " + "(?P<solveP>\S*)" + ".*?" +
                "projectionStep:\ " + "(?P<project>\S*)" + ".*?",
                re.DOTALL)

    caseInfoMatch = caseInfoKey.finditer(content)

    for i, match in enumerate(caseInfoMatch):
        dataBlock = match.groupdict()


    if dataBlock == -1:
        raise NoInfoError("No case info was found!")

    
    for key in dataBlock.keys():
        dataBlock[key] = float(dataBlock[key]) / uConvert[unit]

    events, dataBlock = rearrangeData(dataBlock)

    return caseName, events, dataBlock


def rearrangeData(dataBlock):
    '''
    Rearrange data dictionaries for plots for GTC
    '''

    events = [
            "Initialization", 
            "Preparing Velocity System", 
            "Solving Velocity System", 
            "Preparing Poisson System", 
            "Solving Poisson System", 
            "Projection Step"]

    dataBlock["Initialization"] = dataBlock.pop("main") + dataBlock.pop("init")
    dataBlock["Preparing Velocity System"] = dataBlock.pop("rhsV")
    dataBlock["Solving Velocity System"] = dataBlock.pop("solveV")
    dataBlock["Preparing Poisson System"] = dataBlock.pop("rhsP")
    dataBlock["Solving Poisson System"] = dataBlock.pop("solveP")
    dataBlock["Projection Step"] = dataBlock.pop("project")

    return events, dataBlock


def parseResultFiles(filePath, unit):
    '''
    Parse a set of performanceSummary.txt.
    '''

    data = {}

    resultFiles = findResultFiles(filePath)

    for f in resultFiles:

        try:

            caseName, events, timings = parseSingleResultFile(f, unit)

        except NoInfoError as e:

            print("\nIn the file " + f + ": " + e.value + "\n")

            choose = input(
                    "Add extension \".broken\" to the broken file " +
                    "and ignore it? (Y/n)")

            if choose != "n":
                os.rename(f, f + ".broken")
            else:
                raise

        data[caseName] = timings

    return data, events

"""
def getBenchmarkData(resultPath, output=True):
    '''
    '''

    resultFiles = findResultFiles(resultPath)

    return parseResultFiles(resultFiles, output)




data = getBenchmarkData("/home/pychuang/Cases/atol_1e-5_short", output=True)

key = ["CPU", "GPU", "Theo"]

case = {
    "CPU": numpy.array(["1 CPU node", "2 CPU node", "4 CPU node", "8 CPU node"]),
    "GPU": numpy.array(["1 GPU node", "2 GPU node", "4 GPU node", "8 GPU node"]),
    "Theo": numpy.array(["1 K40c", "2 K40c"])}

events = numpy.array(
        ["Initialization", 
         "Preparing Velocity System", 
         "Solving Velocity System", 
         "Preparing Poisson System", 
         "Solving Poisson System", 
         "Projection Step"])

nProcs = {"GPU": [2, 4, 8, 16], "CPU": [12, 24, 48, 96], "Theo": [1, 2]}
timing = {"GPU": {}, "CPU": {}, "Theo": {}}

for plat in key:
    timing[plat][events[0]] = \
        numpy.array([data[plat][i]["main"] for i in nProcs[plat]])
    timing[plat][events[0]] += \
        numpy.array([data[plat][i]["init"] for i in nProcs[plat]])
    timing[plat][events[1]] = \
        numpy.array([data[plat][i]["rhsV"] for i in nProcs[plat]])
    timing[plat][events[2]] = \
        numpy.array([data[plat][i]["solveV"] for i in nProcs[plat]])
    timing[plat][events[3]] = \
        numpy.array([data[plat][i]["rhsP"] for i in nProcs[plat]])
    timing[plat][events[4]] = \
        numpy.array([data[plat][i]["solveP"] for i in nProcs[plat]])
    timing[plat][events[5]] = \
        numpy.array([data[plat][i]["project"] for i in nProcs[plat]])
    timing[plat]["total"] = \
        numpy.array([data[plat][i]["total"] for i in nProcs[plat]])


plotOrder = [4, 2, 3, 1, 5, 0]


# plot
fig = pyplot.figure(figsize=(12, 8), dpi=150)
gs = gridspec.GridSpec(1, 3, width_ratios=[2, 2, 1])

for i in range(len(key)):

    ax = pyplot.subplot(gs[i])

    color_cycle = ax._get_lines.prop_cycler

    bw = 0.5
    bLoc = numpy.arange(1, len(nProcs[key[i]])+1) - 0.25
    bOffSet = numpy.zeros(len(nProcs[key[i]]))

    for order in plotOrder:

        ax.bar(bLoc, timing[key[i]][events[order]], bw, 
            label=events[order], bottom=bOffSet, 
            color=next(color_cycle)['color'], lw=0, zorder=10)

        bOffSet += timing[key[i]][events[order]]

    for j in range(len(nProcs[key[i]])):
        ax.annotate(
                str(numpy.around(
                    timing["CPU"]["total"][0] /
                    timing[key[i]]["total"][j], 1))+"x", 
                xy=(bLoc[j], timing[key[i]]["total"][j]),
                xytext=(bLoc[j], 
                    timing[key[i]]["total"][j]+timing[key[i]]["total"].max()*0.01),
                fontsize=18, weight="bold", color="red")



    if key[i] == "Theo":
        ax.set_title("Using Workstation", fontsize=16, fontweight="bold")
    else:
        ax.set_title("Using " + key[i] + " Nodes", fontsize=16, fontweight="bold")

    ax.set_ylim(0, timing[key[i]]["total"].max() * 1.1)
    ax.set_ylabel("Time (hour)", fontsize=16, fontweight="bold")
    ax.tick_params(axis="y", labelsize="16")
    ax.yaxis.grid(zorder=0)

    ax.set_xlim(0.5, bLoc[-1]+0.75)
    ax.set_xticks(bLoc)
    ax.set_xticklabels(case[key[i]], fontsize=16, rotation=345, ha="left")


    bars, labels = ax.get_legend_handles_labels()



fig.suptitle("Flying Snake, 2D, Re=2000, AoA=35", 
        fontsize=24, fontweight="bold", y=0.95)


pyplot.figlegend(bars, labels, ncol=3, 
        loc=8, bbox_to_anchor=[0.5, 0.015],
        fontsize=14)

pyplot.subplots_adjust(top=0.85, bottom=0.2, left=0.08, right=0.96, wspace=0.3)
pyplot.savefig("flyingSnake.png", figsize=(10, 8), dpi=150)
"""

