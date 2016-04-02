# coding: utf-8

'''
plot all figure from resulting data
'''

import os
from matplotlib import pyplot
from readCylinder2dRe40 import plotCylinderFigs

fDir = os.path.dirname(os.path.realpath(__file__))

pyplot.style.use(fDir + '/style')

plotCylinderFigs(fDir + "/../../data/cylinder2d_Re40", fDir + "/../", True)

