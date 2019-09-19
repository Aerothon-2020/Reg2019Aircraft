#==============================================================================#
# TITLE
#==============================================================================#
# University of Cincinnati
# Aerocats - Regular Class 2016
# ControlsTable.py: 
#
# update log:
#    11/13/2015 - shiggins: original version
#    01/18/2016 - shiggins: transition to ATLAS
#    11/13/2016 - dechellis: transition to BAP
#
#==============================================================================#
# IMPORTS
#==============================================================================#
# import built-in modules
import os
import sys
import time
import pylab as pyl
import numpy as npy
import cmath as math

# import Aerothon modules
from scalar.units import IN, LBF, ARCDEG, SEC
from scalar.units import AsUnit
from Aerothon.ACControls import ACControls

# import BAP .. dont delete
AVLDir = 'AVL/'
dir_path = os.path.dirname(os.path.realpath(__file__))
parent=dir_path[:-17]
sys.path.append(parent)
from Reg2019Aircraft.aircraft_carter import Aircraft

# go back to the working directory


startTime = time.time() # mark start of simulation

#==============================================================================#
# REVAMPED AEROTHON CLASSES
#==============================================================================#
#ACBatchRun

#==============================================================================#
# CONTROLS TABLE
#==============================================================================#
Execute = True

# Set-up AVL Controls Run
Controls = ACControls(Aircraft)

#Controls.StaticMargin = 0.10
Controls.RunDir = AVLDir # because we redirected to the BAP directory
Controls.AddRun('Stab','AVLAircraft.avl', WriteAVLInput = Execute)
Controls.Stab.AddCommand('a a ' + str(Aircraft.Alpha_Zero_CM/ARCDEG) )
Controls.Stab.DumpStability('AVLDeriv.txt')
Controls.Stab.Exit()

if Execute:
    Controls.ExecuteAVL()

Controls.ReadAVLFiles()

Deriv = Controls.Deriv[0]

#==============================================================================#
# VISUALIZATION & RESULTS
#==============================================================================#

Aircraft.PlotTailLoad(fig=1)
Deriv.StabilityTable(fig=2)
Deriv.PlotStability(fig=3)
t = npy.linspace(0,2)*SEC
#Deriv.PlotPitchResponseDueToElevator(10 * ARCDEG, t, 'Elevator', fig = 4)
Deriv.ControlsTables(fig=5)
Aircraft.Draw(6)

Ma = Deriv.Ma()
Mq = Deriv.Mq()
Madot = Deriv.Madot()

print
print 'AIRCRAFT PROPERTIES'
print 'Lift of AoA     : ', AsUnit(Aircraft.GetAlphaFus_LO(),'deg' )
print 'Zero CM AoA     : ', AsUnit(Aircraft.Alpha_Zero_CM,'deg' )
print
print 'AIRCRAFT DIMENSIONS'
Length = max(Aircraft.HTail.X[0]+(0.75*Aircraft.HTail.Chord(0*IN)),\
             Aircraft.VTail.X[0]+(0.75*Aircraft.VTail.Chord(0*IN)))
Width = Aircraft.Wing.b
Height = Aircraft.VTail.Tip()[2]
print 'Length: ', AsUnit(Length,'in')
print 'Width : ', AsUnit(Width,'in')
print 'Height: ', AsUnit(Height,'in')
print 'TOTAL : ', AsUnit(Length+Height+Width,'in')
print    
print '----- Horiz Tail -----'
print 'HTail VC        : ', AsUnit(Aircraft.HTail.VC)
print 'HTail AR        : ', Aircraft.HTail.AR
print 'HTail Area      : ', AsUnit(Aircraft.HTail.S,'in**2')
print 'HTail Chord     : ', AsUnit(Aircraft.HTail.Chord(0*IN),'in')
print 'HTail Length    : ', AsUnit(Aircraft.HTail.L,'in')
print 'HTail Incidence : ', AsUnit(Aircraft.HTail.i,'deg')
print '----- Vert Tail ------'
print 'Vertical Tail H : ', AsUnit(Aircraft.VTail.Tip()[2],'in' )
print 'VTail VC        : ', AsUnit(Aircraft.VTail.VC)
print 'VTail AR        : ', Aircraft.VTail.AR
print 'VTail Area      : ', AsUnit(Aircraft.VTail.S,'in**2')
print 'VTail Chord     : ', AsUnit(Aircraft.VTail.Chord(0*IN),'in')
print 'VTail Length    : ', AsUnit(Aircraft.VTail.L,'in')
print
print 'S&C PROPERTIES'
print 'Steady state roll rate: ', AsUnit( Deriv.RollDueToAileron(15 * ARCDEG, 'Aileron'), 'deg/s' )
print 'Steady state pitch rate: ', Deriv.PitchResponseDueToElevator(10 * ARCDEG, 1*SEC, 'Elevator')*180/math.pi
print 'Yaw Damping : ', Deriv.Np()
print 'AVL Xnp      : ', Deriv.Xnp, 'in'
print 'Aircraft Xnp : ', AsUnit( Aircraft.Xnp(), 'in' )
#print 'Horizontal Tail incidence angle  : ', AsUnit( Aircraft.HTail.i, 'deg' )
print
print 'AVL Cma, Ma    : ', Deriv.Cma, Ma
print 'AVL Ma**0.5    : ', (-Ma)**0.5
print 'AVL sqrt(Ma)   : ', math.sqrt(-Ma/(1/SEC**2) )
print 'AVL Cmq, Mq    : ', Deriv.Cmq, Mq
print 'AVL Madot      : ', Madot
print -((Mq + Madot) / (2 * (-Ma)**0.5 ))
print
print 'Aircraft Cmadot   : ', Aircraft.Cmadot()
print 'Aircraft Cmq      : ', Aircraft.Cmq()

#print 'Spiral Mode: ', Deriv.SpiralMode()
#print 'Spiral double time: ', Deriv.SpiralDoubleTime()
#print 'AVL Clr    : ', Deriv.Clr
#print 'AVL Clb    : ', Deriv.Clb
#print 'AVL Cnr    : ', Deriv.Cnr
#print 'AVL Cnb    : ', Deriv.Cnb

endTime = time.time() # mark the end of the simulation
print
print 'Controls table calculations completed. Time elapsed: ' + \
      str(round(endTime - startTime,3))

pyl.show()
