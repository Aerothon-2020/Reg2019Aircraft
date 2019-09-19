from __future__ import division # let 5/2 = 2.5 rather than 2

#
# The following line turns off unit checking. Make sure things are working before it is turned off
#
from os import environ as _environ; _environ["scalar_off"] = "off"


import numpy as npy
import pylab as pyl
from scalar.units import FT, SEC, LBF, MIN, IN, ARCDEG
from Aircraft_Models.Adv2014Aircraft_AeroCats.MonoWing.Aircraft import Aircraft
#from Aircraft_Models.Reg2012Aircraft_AeroCats.MonoWing.Aircraft import Aircraft
#from Aircraft_Models.Reg2012Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_40 import Aircraft
#from Aircraft_Models.Reg2012Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_42 import Aircraft
#from Aircraft_Models.Reg2012Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_44 import Aircraft
#from Aircraft_Models.Reg2012Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_46 import Aircraft
#from Aircraft_Models.Reg2012Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_48 import Aircraft
#from Aircraft_Models.Reg2012Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_50 import Aircraft
#from Aircraft_Models.Reg2012Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_52 import Aircraft
#from Aircraft_Models.Reg2012Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_55 import Aircraft
#from Aircraft_Models.Reg2012Aircraft_AeroCats.TradeStudies.LowMoment.Aircraft import Aircraft

Aircraft.Draw(fig=4)
fig_wing = 1
fig_htail = 2
fig_vtail = 3

CD = [0,0,0]

Aircraft.Wing.o_eff = None
#
# Get the design point
#
dsgnGR = Aircraft.Groundroll() / (FT)

V=Aircraft.GetV_LO() + 0.1*FT/SEC
a2dw = Aircraft.AlphaTrim(V)
a2dw = 0*ARCDEG
Re = Aircraft.Wing.Re()
del_e = Aircraft.del_e_trim(a2dw)
CD, junk = Aircraft._CDComponents(a2dw, del_e, V)
#CD[0], CD[1], CD[2] = Aircraft.Wing.af.Cd(a2dw, Re), Aircraft.Wing.CDi(a2dw), Aircraft.Wing.o_eff

pyl.figure(fig_wing); pyl.plot([CD[fig_wing-1]],[dsgnGR],'ro', markersize = 8)
pyl.figure(fig_htail); pyl.plot([CD[fig_htail-1]],[dsgnGR],'ro', markersize = 8)
pyl.figure(fig_vtail); pyl.plot([CD[fig_vtail-1]],[dsgnGR],'ro', markersize = 8)

#
# Set up ranges
#
S    = npy.linspace(906,1600,3)*IN**2
Span = npy.linspace(66,90,3)*IN

lgnd = ['Design W = %2.0f (lbf)' % (Aircraft.TotalWeight / LBF)]
arealist = []

# Initialize data arrays
grndroll = npy.zeros((len(Span),len(S)))
drag = npy.zeros((len(Span),len(S),5))

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
        
        V=Aircraft.GetV_LO() + 0.1*FT/SEC
        a2dw = Aircraft.AlphaTrim(V)
        a2dw = 0*ARCDEG
        del_e = Aircraft.del_e_trim(a2dw)
        drag[ii][jj], junk = Aircraft._CDComponents(a2dw, del_e, V)
        #drag[ii][jj][0], drag[ii][jj][1], drag[ii][jj][2] = Aircraft.Wing.af.Cd(a2dw, Re), Aircraft.Wing.CDi(a2dw), Aircraft.Wing.o_eff

#
# Plot the calculated values
#
for ii in range(len(Span)):
    wing = []
    htail = []
    vtail = []
    grnplt = []
    for jj in range(len(S)):
        wing.append(drag[ii][jj][fig_wing-1])
        htail.append(drag[ii][jj][fig_htail-1])
        vtail.append(drag[ii][jj][fig_vtail-1])
        grnplt.append(grndroll[ii][jj])
        
    pyl.figure(fig_wing); pyl.plot(wing,grnplt,ls = '--', lw = 2)        
    pyl.figure(fig_htail); pyl.plot(htail,grnplt,ls = '--', lw = 2)        
    pyl.figure(fig_vtail); pyl.plot(vtail,grnplt,ls = '--', lw = 2)        
    lgnd.append('b = %2.0f (in)' % (Span[ii] / IN))
    
for jj in range(len(S)):
    wing = []
    htail = []
    vtail = []
    grnplt = []
    for ii in range(len(Span)):
        wing.append(drag[ii][jj][fig_wing-1])
        htail.append(drag[ii][jj][fig_htail-1])
        vtail.append(drag[ii][jj][fig_vtail-1])
        grnplt.append(grndroll[ii][jj])
    
    pyl.figure(fig_wing); pyl.plot(wing,grnplt, lw = 2)        
    pyl.figure(fig_htail); pyl.plot(htail,grnplt, lw = 2)        
    pyl.figure(fig_vtail); pyl.plot(vtail,grnplt, lw = 2)        
    lgnd.append('S = %4.0f (in^2)' % (S[jj] / IN**2))

#lgnd.append('W = %2.0f (lbf)' % (Aircraft.TotalWeight / LBF))

#pyl.axvline(x = 100, color = 'k', lw = 1)
for fig in [1,2,3]:
    pyl.figure(fig)
    pyl.plot()
    pyl.axhline(y = 190, color = 'k', lw = 1)
    pyl.title('Groundroll and Climb Rate for Varying Wing Area and Span')
    pyl.xlabel('Drag at V_LO (LBF)') ; pyl.ylabel('Groundroll (ft)')
    pyl.legend(lgnd, loc = 'best', numpoints=1, labelspacing = 0.0)

pyl.show()