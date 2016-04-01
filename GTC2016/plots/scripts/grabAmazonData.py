# coding: utf-8

'''
grabData.py
'''

import os
import re
import numpy
from matplotlib import pyplot
from matplotlib import gridspec

pyplot.style.use('style')


class NoInfoError(Exception):
    '''
    '''
    def __init__(self, _value="No info found!"):
        '''
        '''
        self.value = _value

    def __str__(self):
        '''
        '''
        return repr(self.value)


def getBenchmarkData(resultPath, output=True):
    '''
    '''

    resultFiles = findResultFiles(resultPath)

    return parseResultFiles(resultFiles, output)



def findResultFiles(resultPath):
    '''
    '''

    resultFiles = []

    for root, dirs, files in os.walk(resultPath):
        for f in files:
            if f == "performanceSummary.txt":
                resultFiles.append(root + "/" + f)

    return resultFiles


def parseResultFiles(resultFiles, output=True):
    '''
    '''

    data = {}

    for f in resultFiles:

        platform, nProc = parseFileName(f, "flyingSnake2dRe2000AoA35_Amazon")

        if platform not in data.keys():
            data[platform] = {}

        f_handle = open(f, "r", encoding="utf-8", errors="replace")
        content = f_handle.read()
        f_handle.close()


        try:

            if output:
                print("parsing " + f + " ...")

            '''
            caseName, dim, mode, algorithm, nprocs, avgTime = \
                parseSingleResultFile(content)
            '''
            timing = parseSingleResultFile(content)

            for key in timing.keys():
                timing[key] = float(timing[key]) / 3600

        except NoInfoError as e:

            print("\nIn the file " + f + ": " + e.value + "\n")

            choose = input(
                    "Add extension \".broken\" to the broken file " +
                    "and ignore it? (Y/n)")

            if choose != "n":
                os.rename(f, f + ".broken")
            else:
                raise

        data[platform][int(nProc)] = timing

    return data


def parseFileName(content, simName):
    '''
    '''
    key = re.compile(simName + "_(?P<nProc>\d*)" + "(?P<platform>GPU|CPU|Theo)")
    match = key.search(content)

    return match.groupdict()["platform"], match.groupdict()["nProc"]


def parseSingleResultFile(content):
    '''
    '''
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

    return dataBlock




data = getBenchmarkData("/home/pychuang/Cases/Amazon", output=True)

case = numpy.array(["8 c4.8xlarge", "1 g2.8xlarge"])

events = numpy.array(
        ["Initialization", 
         "Preparing Velocity System", 
         "Solving Velocity System", 
         "Preparing Poisson System", 
         "Solving Poisson System", 
         "Projection Step"])

timing = {}

timing[events[0]] = \
    numpy.array([data["CPU"][96]["main"], data["GPU"][4]["main"]])
timing[events[0]] += \
    numpy.array([data["CPU"][96]["init"], data["GPU"][4]["init"]])
timing[events[1]] = \
    numpy.array([data["CPU"][96]["rhsV"], data["GPU"][4]["rhsV"]])
timing[events[2]] = \
    numpy.array([data["CPU"][96]["solveV"], data["GPU"][4]["solveV"]])
timing[events[3]] = \
    numpy.array([data["CPU"][96]["rhsP"], data["GPU"][4]["rhsP"]])
timing[events[4]] = \
    numpy.array([data["CPU"][96]["solveP"], data["GPU"][4]["solveP"]])
timing[events[5]] = \
    numpy.array([data["CPU"][96]["project"], data["GPU"][4]["project"]])
timing["total"] = \
    numpy.array([data["CPU"][96]["total"], data["GPU"][4]["total"]])


plotOrder = [4, 2, 3, 1, 5, 0]


# plot
fig = pyplot.figure(figsize=(10, 8), dpi=150)
ax = fig.gca()
color_cycle = ax._get_lines.prop_cycler
bw = 0.5
bLoc = numpy.arange(1, case.size+1) - 0.25
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

pyplot.savefig("Amazon.png", figsize=(10, 8), dpi=150)

