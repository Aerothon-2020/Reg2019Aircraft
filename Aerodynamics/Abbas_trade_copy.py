from os import environ as _environ; _environ["scalar_off"] = "off"

from Aerothon.ACControls import ACControls
from Aerothon import AeroUtil
#from Reg2014Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_NickSchwartz import Aircraft
from Reg2019Aircraft.aircraft_carter import Aircraft
from scalar.units import SEC, ARCDEG, LBF, IN, FT
from scalar.units import AsUnit
import pylab as pyl
import numpy as npy

Wing = Aircraft.Wing
Wing.S = 3300*IN**2
y = npy.linspace(-Wing.b/2/IN, Wing.b/2/IN, 61)*IN

print "Wingspan  : ", Wing.b/2/IN

legend = [];

# Fbs = npy.linspace(0.65,0.65,1)
# TRs = npy.linspace(0.5,0.6,11)
# for Fb in Fbs:
#     Aircraft.Wing.Fb=[Fb,1]
#     for TR in TRs:
#         Aircraft.Wing.TR=[1,TR]
#         #Aircraft,Wing.Draw(fig = 3)
#         LLT = Aircraft.Wing.LLT
#         print("Fb of {}, TR of {}".format(Fb,TR))
#         print "Wing Area : ", AsUnit(Aircraft.Wing.S, 'in**2')
#         print "Wing CL   : ", LLT.CL()
#         pyl.figure(4)
#         pyl.plot(y/IN,LLT.Cl(y))
#         pyl.xlabel("y (in)")
#         pyl.ylabel('Cl')
#         legend.append("TR = " + str(TR) + ",Fb = " + str(Fb))

        
#pyl.axvline(x=Wing.Aileron.Tip()/IN)
#pyl.axvline(x=Wing.Aileron.Root()/IN)
#pyl.legend(legend, loc = 1)
#pyl.plt.grid(True)
#pyl.plt.ylim(1,1.6)
#pyl.show()        
#  Selected Wing Design
#  TR=0.4 Fb=0.45
print("Chosen Design")
Aircraft.Wing.Fb=[0.66,1]
Aircraft.Wing.TR=[1,0.5]
Aircraft.Wing.Draw(fig = 1)
LLT  = Aircraft.Wing.LLT
print "Wing Area   : ", AsUnit(Aircraft.Wing.S, 'in**2' )
print "Wing CL     : ", LLT.CL()
print "Wing Span   : ", Wing.b/IN
pyl.figure(5)
pyl.plot(y/IN, LLT.Cl(y))
pyl.xlabel("y (in)")
pyl.ylabel("$C_l$")
legend.append("Current Design")
print "Oswald Eff. : ", LLT.OswaldEff()

#print "CL's"
#print LLT.Cl(y)
#print "y's"
#print y

# 2015 Original Wing
# Aircraft.Wing.Fb=[0.65,1]
# Aircraft.Wing.TR=[1,0.5]
# Aircraft.Wing.Draw(fig = 1)
# LLT = Aircraft.Wing.LLT
# print " "
# print "2015 Original Wing"
# print "Wing Area   : ", AsUnit(Aircraft.Wing.S, 'in**2' )
# print "Wing CL     : ", LLT.CL()
# print "Wing Span   : ", Wing.b/IN
# pyl.figure(5)
# pyl.plot(y/IN, LLT.Cl(y))
# pyl.xlabel("y (in)")
# pyl.ylabel("$C_l$")
# legend.append("Original Design")
# print "Oswald Eff. : ", LLT.OswaldEff()

# Rectangular Wing
print " "
print "Rectangular Wing"
Aircraft.Wing.TR = [1.0,1.0]
Aircraft.Wing.Draw(fig = 1)
LLT = Aircraft.Wing.LLT
print "Wing Area   : ", AsUnit(Aircraft.Wing.S, 'in**2' )
print "Wing CL     : ", LLT.CL()
pyl.figure(5)
pyl.plot(y/IN, LLT.Cl(y))
pyl.xlabel("y (in)")
pyl.ylabel("$C_l$")
legend.append("Rectangular Wing")
print "Oswald Eff. : ", LLT.OswaldEff()

#  Elliptic Approximation using single sections of constant taper
print " "
print "Elliptic Approximation Wing"
Aircraft.Wing.Fb      = [0.001,1]
Aircraft.Wing.TR = [1.0,0.45] #"Elliptic"
Aircraft.Wing.Draw(fig = 1)
LLT = Aircraft.Wing.LLT
print "Wing Area   : ", AsUnit(Aircraft.Wing.S, 'in**2' )
print "Wing CL     : ", LLT.CL()
pyl.figure(5)
pyl.plot(y/IN, LLT.Cl(y))
pyl.xlabel("y (in)")
pyl.ylabel("$C_l$")
legend.append("Elliptic Approx.")
print "Oswald Eff. : ", LLT.OswaldEff()

# pyl.axvline(x=Wing.Aileron.Tip()/IN)
# pyl.axvline(x=Wing.Aileron.Root()/IN)
pyl.legend(legend, loc = 8)
pyl.plt.grid(True)
pyl.plt.ylim(0,1.45)

# #################CD PLOTS######################
# #  Current Wing Design
# print("Current Wing Design")
# Aircraft.Wing.Fb=[0.66,1]
# Aircraft.Wing.TR=[1,0.5]
# Aircraft.Wing.Draw(fig = 1)
# LLT  = Aircraft.Wing.LLT
# print "Wing Area   : ", AsUnit(Aircraft.Wing.S, 'in**2' )
# print "Wing CD     : ", LLT.CD()
# print "Wing Span   : ", Wing.b/IN
# pyl.figure(6)
# pyl.plot(y/IN, LLT.Cd(y))
# pyl.xlabel("y (in)")
# pyl.ylabel("$C_d$")
# legend.append("Current Design")
# print "Oswald Eff. : ", LLT.OswaldEff()
# 
# # 2015 Original Wing
# Aircraft.Wing.Fb=[0.65,1]
# Aircraft.Wing.TR=[1,0.5]
# Aircraft.Wing.Draw(fig = 1)
# LLT = Aircraft.Wing.LLT
# print " "
# print "2015 Original Wing"
# print "Wing Area   : ", AsUnit(Aircraft.Wing.S, 'in**2' )
# print "Wing CD     : ", LLT.CD()
# print "Wing Span   : ", Wing.b/IN
# pyl.figure(6)
# pyl.plot(y/IN, LLT.Cd(y))
# pyl.xlabel("y (in)")
# pyl.ylabel("$C_d$")
# legend.append("Original Design")
# print "Oswald Eff. : ", LLT.OswaldEff()
# 
# # Rectangular Wing
# print " "
# print "Rectangular Wing"
# Aircraft.Wing.TR = [1.0,1.0]
# Aircraft.Wing.Draw(fig = 1)
# LLT = Aircraft.Wing.LLT
# print "Wing Area   : ", AsUnit(Aircraft.Wing.S, 'in**2' )
# print "Wing CD     : ", LLT.CD()
# pyl.figure(6)
# pyl.plot(y/IN, LLT.Cd(y))
# pyl.xlabel("y (in)")
# pyl.ylabel("$C_d$")
# legend.append("Rectangular Wing")
# print "Oswald Eff. : ", LLT.OswaldEff()
# 
# #  Elliptic Approximation using single sections of constant taper
# print " "
# print "Elliptic Approximation Wing"
# Aircraft.Wing.Fb      = [0.001,1]
# Aircraft.Wing.TR = [1.0,0.45] #"Elliptic"
# Aircraft.Wing.Draw(fig = 1)
# LLT = Aircraft.Wing.LLT
# print "Wing Area   : ", AsUnit(Aircraft.Wing.S, 'in**2' )
# print "Wing CD     : ", LLT.CD()
# pyl.figure(6)
# pyl.plot(y/IN, LLT.Cd(y))
# pyl.xlabel("y (in)")
# pyl.ylabel("$C_d$")
# legend.append("Elliptic Approx.")
# print "Oswald Eff. : ", LLT.OswaldEff()
# 
# pyl.legend(legend, loc = 9)#8)
# pyl.plt.grid(True)
# pyl.plt.ylim(0.01,0.055)#0,1.45)

pyl.show()