from Aerothon.ACAirfoil import ACAirfoil
import pylab as pyl

Airfoils = ["S1223","S1223_TC","E423"]#Main wing
# Airfoils = ["NACA6413","E169", "NACA0015"]
#Airfoils = ["E220", "E221", "E222"]#Horz tail
#Airfoils = ["NACA0010","NACA0012","NACA0015"]#vert tail
#
for AirfoilName in Airfoils:
    Airfoil = ACAirfoil(AirfoilName)
    Airfoil.PlotReportPolars(fig=1, Re=500000)#main wing
#    Airfoil.PlotReportPolars(fig=1, Re=200000)#tail horz and vert
    
pyl.subplot(311)
pyl.legend(Airfoils, loc = "best")


pyl.show()