from __future__ import division # let 5/2 = 2.5 rather than 2

#
# The following line turns off unit checking. Make sure things are working before it is turned off
#
from os import environ as _environ; _environ["scalar_off"] = "off"


import numpy as npy
import pylab as pyl
from scalar.units import FT, SEC, LBF, MIN, IN, ARCDEG
from Aircraft_Models.Adv2014Aircraft_AeroCats.MonoWing.CopyofAircraft import Aircraft

Aircraft.Draw(fig=2)

pyl.figure(1)
# Climb Rate (x) and Groundroll (y)
# Get the design point
#
dsgnGR = Aircraft.Groundroll() / (FT)
dsgnCR = Aircraft.Rate_of_Climb() / (FT/MIN)
pyl.plot([dsgnCR],[dsgnGR],'ro', markersize = 8)

pyl.figure(3)
# Lift-Off Speed (x) and Aircraft Weight
# Plot the current design point
#
dsgnVLO = Aircraft.GetV_LO() / (FT/SEC)
dsgnWE = Aircraft.EmptyWeight / (LBF)
pyl.plot([dsgnVLO],[dsgnWE],'ro', markersize = 8)
#
pyl.figure(4)
# Climb Rate (x) and Lift-Off Speed (y)
# Plot the current design point
#
pyl.plot([dsgnCR],[dsgnVLO],'ro', markersize = 8)
#
# Set up ranges
#
S    = npy.linspace(1100,1300,5)*IN**2
Span = npy.linspace(65,75,5)*IN

lgnd = ['Design W = %2.0f (lbf)' % (Aircraft.TotalWeight / LBF)]
arealist = []

# Initialize data arrays
grndroll = npy.zeros((len(Span),len(S)))
clmbrate = npy.zeros((len(Span),len(S)))
TkoffV   = npy.zeros((len(Span),len(S)))
ACWeight = npy.zeros((len(Span),len(S)))

#
# Calculate the groundroll and climb rate
#
for ii in range(len(Span)):
    print "Calculating at Span = ", Span[ii]/IN
    for jj in range(len(S)):
        print "Calculating at S = ", S[jj]/IN**2
        Aircraft.Wing.S = S[jj]
        Aircraft.Wing.b = Span[ii]
        
        grndroll[ii][jj] = Aircraft.Groundroll() / (FT)
        clmbrate[ii][jj] = Aircraft.Rate_of_Climb() / (FT/MIN)
        TkoffV[ii][jj]   = Aircraft.GetV_LO() / (FT/SEC)  # Added By Brock Pleiman 11/2/13
        ACWeight[ii][jj] = Aircraft.EmptyWeight / (LBF)   # Added By Brock Pleiman 11/2/13
        
        print "Climb Rate = ", clmbrate[ii][jj]
        print "Take off Velocity = ",TkoffV[ii][jj]
        print "A/c Weight = ",ACWeight[ii][jj]

#
# Plot the calculated values 
# Ground Roll and Climb rate
pyl.figure(1)
for ii in range(len(Span)):
    clmplt = []
    grnplt = []
    for jj in range(len(S)):
        clmplt.append(clmbrate[ii][jj])
        grnplt.append(grndroll[ii][jj])
        
    pyl.plot(clmplt,grnplt,ls = '--', lw = 2)        
    lgnd.append('b = %2.0f (in)' % (Span[ii] / IN))
    
for jj in range(len(S)):
    clmplt = []
    grnplt = []
    for ii in range(len(Span)):
        clmplt.append(clmbrate[ii][jj])
        grnplt.append(grndroll[ii][jj])
    
    pyl.plot(clmplt,grnplt, lw = 2)        
    lgnd.append('S = %4.0f (in^2)' % (S[jj] / IN**2))

#lgnd.append('W = %2.0f (lbf)' % (Aircraft.TotalWeight / LBF))

pyl.plot()
#pyl.axhline(y = 250, color = 'k', lw = 1)
#pyl.axvline(x = 400, color = 'k', lw = 1)
pyl.title('Groundroll and Climb Rate for Varying Wing Area and Span')
pyl.xlabel('Climb Rate (ft/min)') ; pyl.ylabel('Groundroll (ft)')
pyl.legend(lgnd, loc = 'best', numpoints=1, labelspacing = 0.0)

# pyl.show()

# Plots
# Weight and Takeoff Velocity
pyl.figure(3)

for ii in range(len(Span)):
    Velplt = []
    acwplt = []
    for jj in range(len(S)):
        Velplt.append(TkoffV[ii][jj])
        acwplt.append(ACWeight[ii][jj])
        
    pyl.plot(Velplt,acwplt,ls = '--', lw = 2)        
    #lgnd.append('b = %2.0f (in)' % (Span[ii] / IN))
    
for jj in range(len(S)):
    Velplt = []
    acwplt = []
    for ii in range(len(Span)):
        Velplt.append(TkoffV[ii][jj])
        acwplt.append(ACWeight[ii][jj])
    
    pyl.plot(Velplt,acwplt, lw = 2)        
    #lgnd.append('S = %4.0f (in^2)' % (S[jj] / IN**2))

#lgnd.append('W = %2.0f (lbf)' % (Aircraft.TotalWeight / LBF))

pyl.plot()
#pyl.axhline(y = 24, color = 'k', lw = 1)
#pyl.axvline(x = 50, color = 'k', lw = 1)
pyl.title('Take-Off Speed and A/C Weight for Varying Wing Area and Span')
pyl.xlabel('Take-Off Speed (ft/sec)') ; pyl.ylabel('A/C Weight (lbf)')
pyl.legend(lgnd, loc = 'best', numpoints=1, labelspacing = 0.0)
#
#
# Climb Rate and Takeoff Velocity
pyl.figure(4)

for ii in range(len(Span)):
    clmplt = []
    Velplt = []    
    for jj in range(len(S)):
        clmplt.append(clmbrate[ii][jj])
        Velplt.append(TkoffV[ii][jj])
        
    pyl.plot(clmplt,Velplt,ls = '--', lw = 2)        
   # lgnd.append('b = %2.0f (in)' % (Span[ii] / IN))
    
for jj in range(len(S)):
    clmplt = []
    Velplt = []
    for ii in range(len(Span)):
        clmplt.append(clmbrate[ii][jj])
        Velplt.append(TkoffV[ii][jj])
    
    pyl.plot(clmplt,Velplt,lw = 2)        
    #lgnd.append('S = %4.0f (in^2)' % (S[jj] / IN**2))

#lgnd.append('W = %2.0f (lbf)' % (Aircraft.TotalWeight / LBF))

pyl.plot()
#pyl.axhline(y = 50, color = 'k', lw = 1)
#pyl.axvline(x = 400, color = 'k', lw = 1)
pyl.title('Climb Rate and Take-Off Speed for Varying Wing Area and Span')
pyl.xlabel('Climb Rate (ft/min)') ; pyl.ylabel('Take-Off Speed (ft/sec)') ; 
pyl.legend(lgnd, loc = 'best', numpoints=1, labelspacing = 0.0)


pyl.show()