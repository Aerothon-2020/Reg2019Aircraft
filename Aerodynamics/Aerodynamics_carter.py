#from os import environ as _environ; _environ["scalar_off"] = "off"

from scalar.units import ARCDEG, IN
from scalar.units import AsUnit
from Reg2019Aircraft.aircraft_carter import Aircraft
import pylab as pyl

Aircraft.PlotDragBuildup(fig=2) 
Aircraft.PlotTrimmedPolars(fig=3)
Aircraft.Wing.PlotDragBuildup(5)
Aircraft.Wing.Draw2DAirfoilPolars(fig=1)

print 'HTail Incidence : ', AsUnit(Aircraft.HTail.i, 'deg')


pyl.show()

