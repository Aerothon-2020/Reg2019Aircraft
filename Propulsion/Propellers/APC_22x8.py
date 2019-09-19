from __future__ import division # let 5/2 = 2.5 rather than 2

# import built-in modules
import os
import sys
import numpy as npy
import cmath as math
import pylab as pyl

# (USER) set-up directories
trunkDir = r'C:\eclipse\workspace\AircraftDesign\trunk'
atlasDir = os.path.join(trunkDir,r'Aircraft_Models\Reg2017Aircraft_BearcatAirlines\BAP')

# link path to Aerothon
sys.path.append(trunkDir)
from Aerothon.ACPropeller import ACPropeller
from Aerothon.AeroUtil import STDCorrection
import numpy as npy
import pylab as pyl
from scalar.units import IN, LBF, SEC, ARCDEG, FT, RPM, OZF, GRAM, gacc, W, K, degR, inHg, MM
from scalar.units import AsUnit

# Set Propeller properties
Prop = ACPropeller()
Prop.name       = 'APC 22x8'
Prop.D          = 22*IN
Prop.Thickness  = 0.5*IN

Prop.Pitch      = 8*IN
Prop.dAlpha     = 11*ARCDEG #### 3.3
Prop.Solidity   = 0.0126  

Prop.AlphaStall = 20*ARCDEG
Prop.AlphaZeroCL = 0*ARCDEG
Prop.CLSlope    = .22/ARCDEG  #- 2D airfoil lift slope .76
Prop.CDCurve    = 2.2          #- 2D curvature of the airfoil drag bucket
Prop.CDp        = .02          #- Parasitic drag

Prop.Weight     = 240*GRAM*gacc

Prop.ThrustUnit = LBF
Prop.ThrustUnitName = 'lbf'
Prop.PowerUnit = W 
Prop.PowerUnitName = 'watt' 
Prop.MaxTipSpeed = None



### These are corrected for a standard day
STD = STDCorrection(29.4*inHg, 293.7*K)

Prop.ThrustData = [(2427 *RPM, 202*OZF*STD),
                   (2322 *RPM, 182*OZF*STD),
                   (2102 *RPM, 146*OZF*STD),
                   (1678 *RPM, 93*OZF*STD),
                   (1387 *RPM, 63*OZF*STD),
                   (98 *RPM, 29*OZF*STD)]






################################################################################
if __name__ == '__main__':
   
    print " D     : ", AsUnit( Prop.D, 'in')
    print " Pitch : ", AsUnit( Prop.Pitch, 'in')
    
    Vmax = 50
    h=0*FT
    N=npy.linspace(1000, 6800, 5)*RPM
    
    Alpha = npy.linspace(-25,25,41)*ARCDEG
    V     = npy.linspace(0,Vmax,30)*FT/SEC
    
    Prop.CoefPlot(Alpha,fig = 1)
    Prop.PTPlot(N,V,h,'V', fig = 2)

#
#    N = npy.linspace(0, 13000,31)*RPM
#    V = npy.linspace(0,Vmax,5)*FT/SEC
#
#    Prop.PTPlot(N,V,h,'N', fig = 3)
    Prop.PlotTestData(fig=4)

    N = 6024*RPM
    print
    print "Static Thrust   : ", AsUnit( Prop.T(N, 0*FT/SEC, h), 'lbf' )
    print "Measured Thrust : ", AsUnit( max(npy.array(Prop.ThrustData)[:,1]), 'lbf' )
    N = 6410*RPM
    print
    print "Static Torque   : ", AsUnit( Prop.P(N, 0*FT/SEC, h)/N, 'in*ozf' )
    print "Measured Torque : ", AsUnit( max(npy.array(Prop.TorqueData)[:,1]), 'in*ozf' )
    
    pyl.show() 
