from __future__ import division # let 5/2 = 2.5 rather than 2
#==============================================================================#
# TITLE
#==============================================================================#
# University of Cincinnati
# Aerocats - Regular Class 2016
# VNDiagram.py: Weight Prediction generation
#
# update log:
#    01/19/2016 - shiggins: original version
#    12/5/2016 - dechellis: modification for BAP
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
BAPDir = os.path.join(trunkDir,r'Aircraft_Models\Reg2017Aircraft_BearcatAirlines\BAP')

# link to Aerothon
sys.path.append(trunkDir)

# import Aerothon modules
from scalar.units import LBF, FT

# import BAP
sys.path.append(BAPDir)
from _aircraft_BAP import Aircraft
from scalar.units import AsUnit

# go back to the working directory
sys.path.append(os.getcwd())

#==============================================================================#
# WEIGHT PREDICTION
#==============================================================================#
#Get maximum score of lift two pounds more than predicted
#Aircraft.TotalWeight = Aircraft.TotalWeight - 2*LBF

TW = 53.0*LBF
EW = 17.17*LBF
h  = Aircraft.Wing.Alt_LO

Aircraft.PlotWeightPrediction(TeamName = 'Bearcat Airlines', 
                              TeamNumber = 016, 
                              fig=1, 
                              TotalWeight = TW, 
                              EmptyWeight = EW, 
                              h = h, 
                              ShowDesign = True)
pyl.show()
