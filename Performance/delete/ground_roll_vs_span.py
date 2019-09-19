from __future__ import division # let 5/2 = 2.5 rather than 2

from os import environ as _environ; _environ["scalar_off"] = "off"

import numpy as npy
import pylab as pyl
from scalar.units import ARCDEG, FT, SEC, LBF, IN
from scalar.units import AsUnit
#from Aircraft_Models.Reg2012Aircraft_AeroCats.MonoWing.Aircraft import Aircraft
#from Aircraft_Models.Reg2012Aircraft_AeroCats.TradeStudies.Performance.WeightTrade.Aircraft_48 import Aircraft
from Aircraft_Models.Adv2014Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_100 import Aircraft
#from Aircraft_Models.Reg2013Aircraft_AeroCats.TradeStudies.Performance.WeightTrade.Aircraft_45 import Aircraft


#print 'Aircraft   V_LO     : ', AsUnit( Aircraft.GetV_LO(), 'ft/s')
#print 'Wing       V_LO     : ',  AsUnit( Aircraft.Wing.GetV_LO(), 'ft/s')
#print 'Ground Roll Distance: ',   AsUnit( Aircraft.Groundroll(), 'ft' )

Spans = npy.linspace(66,100,5)*IN

legend = []
for span in Spans:
    Aircraft.Wing.b = span
    legend += [AsUnit(span, 'in')]
    Aircraft.PlotPropulsionPerformance(1, Vmax = 70*FT/SEC)

pyl.subplot(131)
pyl.legend(legend + ['Thrust'])
pyl.subplot(132)
pyl.legend()
pyl.subplot(133)
pyl.legend(legend)

#Aircraft.Draw(ii+1)

pyl.show()