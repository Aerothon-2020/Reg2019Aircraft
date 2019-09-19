from __future__ import division # let 5/2 = 2.5 rather than 2
#from os import environ as _environ; _environ["scalar_off"] = "off"
#==============================================================================#
# TITLE
#==============================================================================#
# University of Cincinnati
# Aerocats - Regular Class 2016
# VNDiagram.py: VN diagram generation
#
# update log:
#    01/19/2016 - shiggins: original version
#
#==============================================================================#
# IMPORTS
#==============================================================================#
# import built-in modules
import os
import sys
import numpy as npy
import pylab as pyl

# (USER) set up directories
trunkDir = r'C:\eclipse\workspace\AircraftDesign\trunk'
atlasDir = os.path.join(trunkDir,r'Aircraft_Models\Reg2016Aircraft_bAIRcats\ATLAS')

# link to Aerothon
sys.path.append(trunkDir)

# link to Aerothon
sys.path.append(trunkDir)

# import Aerothon modules
from scalar.units import LBF

# import ATLAS
sys.path.append(atlasDir)
from _aircraft_ATLAS import Aircraft

# go back to the working directory
sys.path.append(os.getcwd())

#==============================================================================#
# VN Diagram code
#==============================================================================#
WeightRange = npy.linspace(37.23,37.23,1)*LBF

Aircraft.PlotVNDiagram(2 , nlimit = 5, TotalWeights = WeightRange)
Aircraft.Draw(1)

pyl.show()
