#==============================================================================#
# TITLE
#==============================================================================#
# University of Cincinnati
# Aerocats - Regular Class 2016
# StaticStability_PolarSlopes.py: script imports aircraft model and plots
#                                 stability info
#
# update log:
#    11/13/2015 - shiggins: original version
#    01/18/2016 - shiggins: transition to ATLAS
#    11/13/2016 - dechellis: transition to BAP
#==============================================================================#
# IMPORTS
#==============================================================================#
# import built-in modules
import os
import sys
import pylab as pyl
# This lets you see the parent directory. Dont delete.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# import Aerothon modules
from scalar.units import ARCDEG, IN
from scalar.units import AsUnit

# import BAP

from Reg2019Aircraft.aircraft_carter import Aircraft

#=============================================================================#
# VISUALIZATION & RESULTS
#=============================================================================#
if __name__ == "__main__":

    # The green linear slope approximations should agree well with the blue polars
    # The slope is adjusted with the *SlopeAt variables
    #
    # The CM vs. alpha curve for the neutral point should be horizontal
    
    Aircraft.Wing.Draw2DAirfoilPolars(fig=1)
    Aircraft.HTail.Draw2DAirfoilPolars(fig=2)

    Aircraft.PlotPolarsSlopes(fig=3)
    Aircraft.PlotCMPolars(4, (-10*ARCDEG, -5*ARCDEG, 0*ARCDEG, +5*ARCDEG, +10*ARCDEG), XcgOffsets=(+0.02, -0.02))

    Aircraft.PlotCLCMComponents(fig = 5, del_es = (-10*ARCDEG, -5*ARCDEG, 0*ARCDEG, +5*ARCDEG, +10 * ARCDEG))

    Aircraft.Refresh()

    print "Xnp             : ", AsUnit( Aircraft.Xnp(), 'in' )
    print "Wing X          : ", AsUnit( Aircraft.Wing.X[0], 'in' )
    print 'HTail Incidence : ', AsUnit(Aircraft.HTail.i, 'deg')
    print 'HTail VC        : ', Aircraft.HTail.VC
    print
    print 'Static stability polar slopes calculations complete.'
   
    pyl.show()
