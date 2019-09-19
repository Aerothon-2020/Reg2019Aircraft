from __future__ import division # let 5/2 = 2.5 rather than 2

from os import environ as _environ; _environ["scalar_off"] = "off"

import numpy as npy
import pylab as pyl
from scalar.units import FT, SEC, LBF, MIN, IN
from scalar.units import AsUnit
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
MinCumpRate = 100
S    = npy.linspace(906,1500,5)*IN**2
WT   = npy.linspace(27,50,1)*LBF

lgnd = ['Design']
arealist = []

# Initialize data arrays
grndroll = npy.zeros((len(WT),len(S)))
clmbrate = npy.zeros((len(WT),len(S)))

#
# Calculate the groundroll and climb rate
#
for ii in range(len(WT)):
    print "Calculating total weight = ", AsUnit( WT[ii], 'lbf' )
    for jj in range(len(S)):
        print "Calculating at S = ", AsUnit( S[jj], 'in**2' )
        Aircraft.Wing.S = S[jj]
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
    for jj in range(len(S)):
        clmplt.append(clmbrate[ii][jj])
        grnplt.append(grndroll[ii][jj])
        
    pyl.plot(clmplt,grnplt,ls = '--', lw = 2)        
    lgnd.append('W = %2.0f (lbf)' % (WT[ii] / LBF))
    
for jj in range(len(S)):
    clmplt = []
    grnplt = []
    for ii in range(len(WT)):
        clmplt.append(clmbrate[ii][jj])
        grnplt.append(grndroll[ii][jj])
    
    pyl.plot(clmplt,grnplt, lw = 2)        
    lgnd.append(r'S = %4.0f (in$^2$)' % (arealist[jj] / IN**2))

pyl.plot()
pyl.axhline(y = 190, color = 'k', lw = 1)
pyl.axvline(x = MinCumpRate, color = 'k', lw = 1)
pyl.title('Groundroll and Climb Rate for Varying Wing Area and Total Weight')
pyl.xlabel('Climb Rate (ft/min)') ; pyl.ylabel('Groundroll (ft)')
pyl.legend(lgnd, loc = 'best', numpoints=1, labelspacing = 0.0)
pyl.ylim( 0, 400 )
pyl.xlim( 50, 350 )

pyl.show()