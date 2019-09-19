#==============================================================================#
# TITLE
#==============================================================================#
# University of Cincinnati
# Aerocats - Regular Class 2016
# HingeMoments.py:
#
# update log:
#    11/20/2015 - shiggins: original version
#    01/18/2016 - shiggins: transition to ATLAS
#    11/14/2016 - dechellis: transition to BAP
#==============================================================================#
# IMPORTS
#==============================================================================#
# import built-in modules
import os
import sys
import pylab as pyl
import numpy as npy

# (USER) set up directories
trunkDir = r'C:\eclipse\workspace\AircraftDesign\trunk'
BAPDir = os.path.join(trunkDir,r'Aircraft_Models\Reg2017Aircraft_BearcatAirlines\BAP')

# link path to Aerothon
sys.path.append(trunkDir)

# import Aerothon modules
from Aerothon.ACControls import ACControls
from Aerothon.ACXFoil import ACXFoil
from Aerothon import AeroUtil
from scalar.units import SEC, ARCDEG, LBF, IN, FT, OZF
from scalar.units import AsUnit

# import BAP
sys.path.append(BAPDir)
from _aircraft_BAP import Aircraft

#==============================================================================#
# HINGE MOMENTS CODE
#==============================================================================#
Execute = True

Vs = npy.linspace(Aircraft.GetV_LO()/(FT/SEC), Aircraft.Vmax()/(FT/SEC), 9)*FT/SEC
des = npy.linspace(5, 25, 5)*ARCDEG
dail = npy.linspace(5, 25, 5)*ARCDEG
alpha2d = 0*ARCDEG

# Use the following to investigate the effects of changing geometry
#Aircraft.Wing.Aileron.Fc = 0.15
#Aircraft.Wing.Aileron.Fb = 0.334 #Need adjusted to make aileron 3% from tip
#Aircraft.Wing.Aileron.Ft = 0.1337

#This are the ratios of the servo arm to the control horn arm. The control arm length is the distance to the hinge.
# ArmRatio = (Servo Arm)/(Control Arm)

Aileron_ArmRatio = 0.5
Elevator_ArmRatio = 1.0
Rudder_ArmRatio = 1.0

#==============================================================================#
# VISUALIZATION & RESULTS
#==============================================================================#
##Aircraft.Wing.Aileron.PlotHingeMoment(fig=1, RunDir='XFoil/Aileron/', alpha2d=alpha2d, Ht=1, ArmRatio=Aileron_ArmRatio, des=des, Vs=Vs, Execute=Execute)
##pyl.title('Aileron Hinge Moment')
##Aircraft.HTail.Elevator.PlotHingeMoment(fig=2, RunDir='XFoil/Elevator/', alpha2d=alpha2d, Ht=1, ArmRatio=Elevator_ArmRatio, des=des, Vs=Vs, Execute=Execute)
##pyl.title('Elevator Hinge Moment')
Aircraft.VTail.Rudder.PlotHingeMoment(fig=3, RunDir='XFoil/Rudder/', alpha2d=alpha2d, Ht=0.5, ArmRatio=Rudder_ArmRatio, des=des, Vs=Vs, Execute=Execute)
pyl.title('Rudder Hinge Moment')

# Aircraft.VTail2.Rudder.PlotHingeMoment(fig=4, RunDir='XFoil/Rudder/', alpha2d=alpha2d, Ht=0.5, ArmRatio=Rudder_ArmRatio, des=des, Vs=Vs, Execute=Execute)
# pyl.title('Outside Rudder Hinge Moment')

pyl.show()
