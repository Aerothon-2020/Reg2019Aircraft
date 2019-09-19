from os import environ as _environ; _environ["scalar_off"] = "off"

from Aerothon.ACControls import ACControls
from Aerothon import AeroUtil
#from Aircraft_Models.Reg2014Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_NickSchwartz import Aircraft
from Reg2019Aircraft.aircraft_carter import Aircraft
from scalar.units import SEC, ARCDEG, LBF, IN, FT
from scalar.units import AsUnit
import pylab as pyl
import numpy as npy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import xxsubtype

#######################################################################################################
################################Area and Span Study####################################################
##########################Outputs 2x2 - Span & Area vs. Cl, Cd, Lift, LoD##############################
#######################################################################################################
#Wing = Aircraft.Wing
#
#legend = [];
#
#bbs = npy.linspace(96,110,15) #Total span lengths
#SSs = npy.linspace(1500,2200,15) #Total wing area
##Span ~= 100 in, wing area ~= 1750 in^2 <--First round through
##Span ~= 100 in, wing area ~= 1750 in^2 <--Second round through still works
#Wing.Lam = [0*ARCDEG,0*ARCDEG] #Sweep angle-1st is sweep from root, 2nd is sweep from Fb location
#Wing.Gam = [0*ARCDEG,0*ARCDEG]
#
#CCLS = []
#CCDS = []
#xxs = []
#yys = []
#LLift = []
#LLoD = []
#
#rho = npy.float(0.002237) #slugs/ft^3  #0.0741 lb/ft^3
##V = 40 #ft/s
#Aircraft.Wing.TR = [1.0,0.50]
#Aircraft.Wing.Fb = [0.66,1.0]
#fig = plt.figure()
#for SS in SSs:
#    Aircraft.Wing.S = SS*IN**2
#    CLS = []
#    CDS = []
#    Lift = []
#    LoD = []
#    xs = []
#    ys= []
#    for bb in bbs:
#        Aircraft.Wing.b = bb*IN
#        Aircraft,Wing.Draw(fig = 5)
#        LLT = Aircraft.Wing.LLT
#        V = Wing.GetV_LO()
#        lift = npy.float(Wing.Lift_LO/5.3697)#4.448222)
#        #print "Lift at LO : ", npy.float(Wing.Lift_LO)
#        #print "lift is: "+str(lift)
#        Lift.append(lift)
#        cl = npy.max(LLT.CL())
#        cd = npy.max(LLT.CD())
#        CLS.append(cl)
#        CDS.append(cd)
#        #Lift.append(0.5*rho*(V**2)*(SS/144)*npy.max(LLT.CL()))
#        print "SS = " + str(SS) + ", bb = " + str(bb)
#        LoD.append(cl/cd)
#        xs.append(bb)
#        ys.append(SS)
#
#        legend.append("S = " + str(SS) + ", b = " + str(bb))
#
#    CCLS.append(CLS)
#    CCDS.append(CDS)
#    LLift.append(Lift)
#    LLoD.append(LoD)
#    xxs.append(xs)
#    yys.append(ys)
#
#ax1 = fig.add_subplot(221, projection='3d')
#ax1.plot_wireframe(xxs, yys, CCLS)
##ax1.set_xlabel('Span (in)')
##ax1.set_ylabel('Wing Area (in^2)')
##ax1.set_zlabel('Lift-Line CL')
#
#ax2 = fig.add_subplot(222, projection='3d')
#ax2.plot_wireframe(xxs, yys, LLift)
##ax2.set_xlabel('Span (in)')
##ax2.set_ylabel('Wing Area (in^2)')
##ax2.set_zlabel('Plane Lift (lbs)')
#
#ax3 = fig.add_subplot(223, projection='3d')
#ax3.plot_wireframe(xxs, yys, CCDS)
##ax3.set_xlabel('Span (in)')
##ax3.set_ylabel('Wing Area (in^2)')
##ax3.set_zlabel('Lift-Line CD')
#
#ax4 = fig.add_subplot(224, projection='3d')
#ax4.plot_wireframe(xxs, yys, LLoD)
##ax4.set_xlabel('Span (in)')
##ax4.set_ylabel('Wing Area (in^2)')
##ax4.set_zlabel('Plane LoD')

#######################################################################################################
##############################Taper Ratio and Taper Location Study#####################################
##########################Outputs 2x2 - Span & Area vs. Cl, Cd, Lift, LoD##############################
#######################################################################################################

Wing = Aircraft.Wing
Wing.b = 105*IN
y = npy.linspace(-Wing.b/2/IN, Wing.b/2/IN, 121)*IN

legend = [];

Fbs = npy.linspace(0.2,0.9,15) #0.2 0.9 8Distance from root chord in % of 1/2 span the taper ratio begins
TRs = npy.linspace(0.2,0.9,15) #Taper ratio beginning at Fb's location. 0.385 at FB =0.45 is most even
#TR is 0.71, Fb = 0.5 <--First round through
#TR is 0.50, Fb is 0.3 <--Second round through
Wing.Lam = [0*ARCDEG,0*ARCDEG] #Sweep angle-1st is sweep from root, 2nd is sweep from Fb location
Wing.Gam = [0*ARCDEG,0*ARCDEG]

xs = []
ys = []
CLs = []
ACL = []
WTCL = []
xxs = []
yys = []
MCLs = []
ACLs = []
WTCLs = []
diff = []
diffs = []

rho = 0.002237 #slugs/ft^3 
V = 38

for Fb in Fbs:
    Aircraft.Wing.Fb = [Fb,1.0]
    for TR in TRs:
        temp = []
        LLT = []
        Aircraft.Wing.TR = [1.0,TR]
        LLT = Aircraft.Wing.LLT
        #Aircraft.Wing.Draw(fig = 2)
        
        #xs.append(Fb)#Taper Break
        #ys.append(TR)#Taper ratio
        temp = LLT.Cl(y)
        last = len(temp) #Total length of Cl values (121)
        #print "Halfway point is " + str(npy.round(last/2))
        for x in range(2,npy.round(last/2)):
            slope1 = temp[x] - temp[x-1]
            slope2 = temp[x+1] - temp[x]
            if slope2 < 0 or (slope2-slope1) > 0.0001:
                wingtipmax = x
                break
                #if slope2 > slope1:
                #    wingtipmax = x-1
                    #print "Wingtipmax at " + str(x)
                #    break
        try:
            wingtipmax
        except NameError:
            wingtipmax = last/2

        WingRootCLMax = temp[last/2]
        WingTipCLMax = temp[wingtipmax]
        diffCl = WingRootCLMax-WingTipCLMax
        
        #CLs.append(WingRootCLMax) #Max CL of wing(at root)
        #ACL.append(npy.average(LLT.Cl(y))) #Average CL across wing
        #WTCL.append(WingTipCLMax) #Identify the maximum value
        #diff.append(WingTipCLMax-WingRootCLMax)
        if diffCl > 0.1 and WingRootCLMax > WingTipCLMax: #and diffCl < 0.3
            #print "WingRootCL is: "+str(WingRootCLMax)+" WingTipCL is: "+str(WingTipCLMax)
            print "Fb: "+str(Fb)+" TR: "+str(TR)+" Diff: "+str(diffCl)
            Aircraft.Wing.Draw(fig = 2)
            xs.append(Fb)#Taper Break
            ys.append(TR)#Taper ratio
            CLs.append(WingRootCLMax) #Max CL of wing(at root)
            ACL.append(npy.average(LLT.Cl(y))) #Average CL across wing
            WTCL.append(WingTipCLMax) #Identify the maximum value
            diff.append(WingRootCLMax-WingTipCLMax) #Difference between root Cl and wingtip Cl
        del wingtipmax
    xxs.append(xs)#Taper Break
    yys.append(ys)#Taper ratio
    MCLs.append(CLs)
    ACLs.append(ACL)
    WTCLs.append(WTCL)
    diffs.append(diff)
    
fig = pyl.figure()
ax1 = fig.add_subplot(221, projection='3d')
#ax1.plot_wireframe(xxs, yys, MCLs)
ax1.scatter(xxs,yys,MCLs, marker=u'.')
ax1.set_ylabel('Taper Ratio')
ax1.set_xlabel('Taper Break')
ax1.set_zlabel('3D $C_L$')
print "Taper Break"
print xxs
print "Taper Ratio"
print yys
print "Max CL"
print MCLs


ax2 = fig.add_subplot(222, projection='3d')
#ax2.plot_wireframe(xxs, yys, ACLs)
ax2.scatter(xxs,yys,ACLs, marker=u'.')
ax2.set_ylabel('Taper Ratio')
ax2.set_xlabel('Taper Break')
ax2.set_zlabel('Average 3D $C_l$')

ax3 = fig.add_subplot(223, projection='3d')
#ax3.plot_wireframe(xxs, yys, WTCLs)
ax3.scatter(xxs,yys,WTCLs, marker=u'.')
ax3.set_ylabel('Taper Ratio')
ax3.set_xlabel('Taper Break')
ax3.set_zlabel('Max Wingtip $C_L$')

ax4 = fig.add_subplot(224, projection='3d')
#ax4.plot_wireframe(xxs, yys, diffs)
ax4.scatter(xxs, yys,diffs, marker=u'.')
ax4.set_ylabel('Taper Ratio')
ax4.set_xlabel('Taper Break')
ax4.set_zlabel('Wing Root - Wing Tip $C_L$')

fig = pyl.figure()
aaa = fig.add_subplot(111, projection='3d')
aaa.scatter(xxs, yys,diffs, marker=u'.')
aaa.set_ylabel('Taper Ratio')
aaa.set_xlabel('Taper Break Location')
aaa.set_zlabel('Max - Tip $C_L$')

###########################TRL vs Z axis Values##########################
fig = pyl.figure()
ax11 = fig.add_subplot(221)#, projection='3d')
#ax11.plot(xxs, MCLs)
ax11.scatter(xxs,MCLs, marker=u'.')
ax11.set_xlabel('Taper Break')
ax11.set_ylabel('3D CL')
ax11.grid()

ax22 = fig.add_subplot(222)#, projection='3d')
#ax22.plot(xxs, ACLs)
ax22.scatter(xxs,ACLs, marker=u'.')
ax22.set_xlabel('Taper Break')
ax22.set_ylabel('Average 3D Cl')
ax22.grid()

ax33 = fig.add_subplot(223)#, projection='3d')
#ax33.plot(xxs, WTCLs)
ax33.scatter(xxs,WTCLs, marker=u'.')
ax33.set_xlabel('Taper Break')
ax33.set_ylabel('Max Wingtip Cl')
ax33.grid()

ax44 = fig.add_subplot(224)#, projection='3d')
#ax44.plot(xxs, diffs)
ax44.scatter(xxs,diffs, marker=u'.')
ax44.set_xlabel('Taper Break')
ax44.set_ylabel('Max - Tip Cl')
ax44.grid()

###########################TR vs Z axis Values##########################
fig = pyl.figure()
ax111 = fig.add_subplot(221)#, projection='3d')
#ax111.plot(yys, MCLs)
ax111.scatter(yys,MCLs, marker=u'.')
ax111.set_xlabel('Taper Ratio')
ax111.set_ylabel('3D CL')
ax111.grid()

ax222 = fig.add_subplot(222)#, projection='3d')
#ax222.plot(yys, ACLs)
ax222.scatter(yys,ACLs, marker=u'.')
ax222.set_xlabel('Taper Ratio')
ax222.set_ylabel('Average 3D Cl')
ax222.grid()

ax333 = fig.add_subplot(223)#, projection='3d')
#ax333.plot(yys, WTCLs)
ax333.scatter(yys,WTCLs, marker=u'.')
ax333.set_xlabel('Taper Ratio')
ax333.set_ylabel('Max Wingtip Cl')
ax333.grid()

ax444 = fig.add_subplot(224)#, projection='3d')
#ax444.plot(yys, diffs)
ax444.scatter(yys,diffs, marker=u'.')
ax444.set_xlabel('Taper Ratio')
ax444.set_ylabel('Max - Tip Cl')
ax444.grid()

#################Original FB vs TR Plots############################

#Wing = Aircraft.Wing
#Wing.b = 100*IN
#y = npy.linspace(-Wing.b/2/IN, Wing.b/2/IN, 121)*IN
#
#legend = [];
#
#Fbs = npy.linspace(0.9,0.9,1) #0.2 0.9 8Distance from root chord in % of 1/2 span the taper ratio begins
#TRs = npy.linspace(0.9,0.9,1) #Taper ratio beginning at Fb's location. 0.385 at FB =0.45 is most even
##TR is 0.71, Fb = 0.5 <--First round through
##TR is 0.50, Fb is 0.3 <--Second round through
#Wing.Lam = [0*ARCDEG,0*ARCDEG] #Sweep angle-1st is sweep from root, 2nd is sweep from Fb location
#Wing.Gam = [0*ARCDEG,0*ARCDEG]
#for Fb in Fbs:
#    Aircraft.Wing.Fb = [Fb,1.0]
#    for TR in TRs:
#        Aircraft.Wing.TR = [1.0,TR]
#        Aircraft.Wing.Draw(fig = 2)
#        LLT = Aircraft.Wing.LLT
#        #Aircraft.Wing.Draw(fig = 2)
#        pyl.figure(1)
#        pyl.plot(y/IN,LLT.Cl(y))
#        pyl.title("Cl Across Span")
#        pyl.xlabel("y (in)")
#        pyl.ylabel('Cl')
#
#        legend.append("Fb = " + str(Fb) + ", TR = " + str(TR))
#        
#        pyl.legend(legend, loc = 1)
#        pyl.plt.grid(True)
#        pyl.plt.ylim(1,1.8)
#       
#        pyl.figure(4)
#        pyl.scatter(Wing.Chord(0*FT),npy.max(LLT.CL()))
##        pyl.figure(2)
#        pyl.plot(y/IN,LLT.Cd(y))
#        pyl.title("Cd Across Span")
#        pyl.xlabel("y (in)")
#        pyl.ylabel('Cd')
#        legend.append("TR = " + str(TR) + ",Fb = " + str(Fb))
#        
#        pyl.axvline(x=Wing.Aileron.Tip()/IN)
#        pyl.axvline(x=Wing.Aileron.Root()/IN)
#        pyl.legend(legend, loc = 1)
#        pyl.plt.grid(True)
#        pyl.plt.ylim(0,0.05)
#        
#        temp = LLT.Cl(y)
#        temp2 = LLT.Cl(y)
#        last = len(temp) #Total length of Cl values (121)
#        print "Halfway point is " + str(npy.round(last/2))
#        for x in range(2, npy.round(last/2)):
#            slope1 = temp[x] - temp[x-1]
#            slope2 = temp[x+1] - temp[x]
#            if slope2 < 0:# or slope1 < slope2:
#                if slope2 > slope1:
#                    wingtipmax = x
#                    print "Wingtipmax at " + str(x)
#                    break
#        try:
#            wingtipmax
#        except NameError:
#            print "well, it WASN'T defined after all!"
#            wingtipmax = 61
#        else:
#            print "sure, it was defined."
#        index = npy.int(wingtipmax) #Identify only the wingtip curve (approximately)
#        index2 = npy.int(last-wingtipmax)
#        #print temp
#        temp[index:last-1] = 0 #Set the unnecessary values to zero
#        temp2[0:index] = 0
#        temp2[index2:-1] = 0
#        #print temp
#        #print temp2
#        print 'Fb : ', Fb, 'TR : ', TR
#        print 'Diff : ',  npy.max(temp2)-npy.max(temp)
#        print 'Max Temp: ',npy.max(temp)
#        print 'Max Temp2: ',npy.max(temp2)
#        print LLT.Cl(y)
#        print temp
#        print temp2
#        if npy.max(temp2)-npy.max(temp) > 0.1:
#            
#            print 'Fb : ', Fb, 'TR : ', TR
#        del wingtipmax
        

#pyl.plt.contour(xs,ys,CLS)
#pyl.plot_wireframe(Fbs, TRs, CLS)

#print "X's : ", y/IN
#print "Fb : ", Fb
#print "CD's : ", LLT.Cd(y)
#print "CL's : ", LLT.Cl(y)

#######################################################################################################
#####################################Original  Study###################################################
#######################################################################################################        
# Selected Wing Design
#TR=0.5 Fb=0.3
#from os import environ as _environ; _environ["scalar_off"] = "off"
#
#from Aerothon.ACControls import ACControls
#from Aerothon import AeroUtil
##from Aircraft_Models.Reg2014Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_NickSchwartz import Aircraft
#from Aircraft_Models.Reg2014Aircraft_AeroCats.MonoWing.Aircraft import Aircraft
#from scalar.units import SEC, ARCDEG, LBF, IN, FT
#from scalar.units import AsUnit
#import pylab as pyl
#import numpy as npy
#
#Aircraft.Wing.b = 100*IN
#Wing = Aircraft.Wing
#y = npy.linspace(-Wing.b/2/IN, Wing.b/2/IN, 121)*IN
#
#print "Halfspan  : ", Wing.b/2/IN
#
#legend = [];
#        
#pyl.axvline(x=Wing.Aileron.Tip()/IN)
#pyl.axvline(x=Wing.Aileron.Root()/IN)
#pyl.legend(legend, loc = 1)
#pyl.plt.grid(True)
#pyl.plt.ylim(1,1.6)
##pyl.show()        
##  Selected Wing Design
##  TR=0.4 Fb=0.45
#print("Selected Wing Design")
#Aircraft.Wing.S = 1750*IN**2
#Aircraft.Wing.Fb = [0.6,1.0]
#Aircraft.Wing.TR = [1.0,0.385]
#Aircraft.Wing.Draw(fig = 1)
#LLT  = Aircraft.Wing.LLT
#print "Wing Area   : ", AsUnit(Aircraft.Wing.S, 'in**2' )
#print "Wing CL     : ", LLT.CL()
#pyl.figure(5)
#pyl.plot(y/IN, LLT.Cl(y))
#pyl.xlabel("y (in)")
#pyl.ylabel("Cl")
#legend.append("Selected Wing Design")        
#
## Rectangular Wing
#Aircraft.Wing.TR = [1.0,1.0]
#Aircraft.Wing.Draw(fig = 2)
#LLT = Aircraft.Wing.LLT
#print "Wing Area   : ", AsUnit(Aircraft.Wing.S, 'in**2' )
#print "Wing CL     : ", LLT.CL()
#pyl.figure(5)
#pyl.plot(y/IN, LLT.Cl(y))
#pyl.xlabel("y (in)")
#pyl.ylabel("Cl")
#legend.append("Rectangular wing")
# 
##  Elliptic Approximation using single sections of constant taper
#Aircraft.Wing.Fb      = [0.001,1]
#Aircraft.Wing.TR = [1.0,0.45] #"Elliptic"
#Aircraft.Wing.Draw(fig = 3)
#LLT = Aircraft.Wing.LLT
#print "Wing Area   : ", AsUnit(Aircraft.Wing.S, 'in**2' )
#print "Wing CL     : ", LLT.CL()
#pyl.figure(5)
#pyl.plot(y/IN, LLT.Cl(y))
#pyl.xlabel("y (in)")
#pyl.ylabel("Cl")
#legend.append("Elliptic Approx.")
#
#pyl.axvline(x=Wing.Aileron.Tip()/IN)
#pyl.axvline(x=Wing.Aileron.Root()/IN)
#pyl.legend(legend, loc = 1)
#pyl.plt.grid(True)
#pyl.plt.ylim(0,1.45)

pyl.show()