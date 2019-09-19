from __future__ import division # let 5/2 = 2.5 rather than 2

#
# The following line turns off unit checking. Make sure things are working before it is turned off
#
from os import environ as _environ; _environ["scalar_off"] = "off"


import numpy as npy
import pylab as pyl
from scalar.units import FT, SEC, LBF, MIN, IN
from Aircraft_Models.Adv2014Aircraft_AeroCats.MonoWing.Aircraft import Aircraft

pyl.figure(1)

#
# Get the design point
#
dsgnGR = Aircraft.Groundroll() / (FT)
dsgnCR = Aircraft.Rate_of_Climb(1.07*Aircraft.GetV_LO()) / (FT/MIN)
pyl.plot([dsgnCR],[dsgnGR],'ro', markersize = 8)

#
# Set up ranges
#
Vstl = npy.linspace(31,35,5)*FT/SEC
WT   = npy.linspace(30,34,5)*LBF
Vplt = Vstl / (FT/SEC)

lgnd = ['Design']
arealist = []

# Initialize data arrays
grndroll = npy.zeros((len(WT),len(Vstl)))
clmbrate = npy.zeros((len(WT),len(Vstl)))

#
# Calculate the groundroll and climb rate
#
for ii in range(len(WT)):
    print "Calculating total weight = ",WT[ii]
    for jj in range(len(Vstl)):
        print "Calculating at Vstl = ",Vstl[jj]
        Aircraft.Wing.V_Stall = Vstl[jj]
        Aircraft.TotalWeight = WT[ii]
        
        grndroll[ii][jj] = Aircraft.Groundroll() / (FT)
        clmbrate[ii][jj] = Aircraft.Rate_of_Climb(1.07*Aircraft.GetV_LO()) / (FT/MIN)
        if ii == 0:
            arealist.append(Aircraft.Wing.S)
        

#
# Plot the calculated values
#        
for ii in range(len(WT)):
    clmplt = []
    grnplt = []
    for jj in range(len(Vstl)):
        clmplt.append(clmbrate[ii][jj])
        grnplt.append(grndroll[ii][jj])
        
    pyl.plot(clmplt,grnplt,ls = '--', lw = 2)        
    lgnd.append('W = %2.0f (lbf)' % (WT[ii] / LBF))
    
for jj in range(len(Vstl)):
    clmplt = []
    grnplt = []
    for ii in range(len(WT)):
        clmplt.append(clmbrate[ii][jj])
        grnplt.append(grndroll[ii][jj])
    
    pyl.plot(clmplt,grnplt, lw = 2)        
    lgnd.append('S = %4.0f (in^2)' % (arealist[jj] / IN**2))

pyl.plot()
pyl.axhline(y = 190, color = 'k', lw = 1)
pyl.axvline(x = 200, color = 'k', lw = 1)
pyl.title('Groundroll and Climb Rate for Varying Wing Area and Total Weight')
pyl.xlabel('Climb Rate (ft/min)') ; pyl.ylabel('Groundroll (ft)')
pyl.legend(lgnd, loc = 'best', numpoints=1, labelspacing = 0.0)

pyl.show()