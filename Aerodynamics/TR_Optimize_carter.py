#from os import environ as _environ; _environ["scalar_off"] = "off"

from Reg2019Aircraft.Aerodynamics.Wing.wing_carter_builder import Wing
from Aerothon.ACLiftingLine import ACLiftingLine
import numpy as npy
import pylab as pyl
from scalar.units import IN, ARCDEG
from scalar.units import AsUnit

#Wing.Airfoil = 'S1223'

LLT = Wing.LLT

SetTR = Wing.TR[1]
SetLoD = LLT.CL()/LLT.CD()
SetCL = LLT.CL()
Sete  = LLT.OswaldEff()

y = npy.linspace(-Wing.b/2/IN, Wing.b/2/IN, 61)*IN

#LLT.nSpan = 101
LLT.Alpha3d = 5*ARCDEG

TRs = npy.linspace(0.1, 0.7, 7)

LoD = {}
CL  = {}
e   = {}

for TR in TRs:

    Wing.TR = [1,TR]

    #LLT.InitEllipticCirculation()
    LoD[TR] = LLT.CL()/LLT.CD()
    CL[TR] = LLT.CL()
    e[TR] = LLT.OswaldEff()
    print
    print 'TR  : ', TR
    print 'CL  : ', LLT.CL()
    print 'CDi : ', LLT.CDi()
    print 'CD  : ', LLT.CD()
    print 'L/D : ', LLT.CL()/LLT.CD()
    print 'e   : ', LLT.OswaldEff()
        

def SetMax(val, max, TR):
    
    if val[TR] > max[0]:
        max[0] = val[TR]
        max[1] = TR

maxLoD = [0,0]
maxCL  = [0,0]
maxe   = [0,0]
for TR in TRs:
    
    SetMax(LoD, maxLoD, TR)
    SetMax(CL , maxCL, TR)
    SetMax(e  , maxe, TR)


def PrintMax(name, max, fig):
    print "Max ", name, '  ', max[0], ', at TR', max[1] 
    Wing.TR = [1,max[1]]
    Wing.Draw(fig=fig)
    pyl.title('Max ' + name)

print
print
PrintMax('LoD', maxLoD, 1)
PrintMax('CL', maxCL, 2)
PrintMax('e', maxe, 3)
print 'Fb : ', Wing.Fb[0]
print 'Set TR :', SetTR, ', LoD ', SetLoD, ', CL ', SetCL, ', e', Sete


pyl.figure(4)
def Plot(values, ylabel):
    vals = [values[TR] for TR in TRs ]
    pyl.plot(TRs, vals)
    pyl.ylabel(ylabel)
    pyl.xlabel('TR')
    pyl.grid()
pyl.subplot(131)
Plot(LoD, 'LoD')
pyl.plot(SetTR, SetLoD, 'o')
pyl.subplot(132)
Plot(CL, 'CL')
pyl.plot(SetTR, SetCL, 'o')
pyl.subplot(133)
Plot(e, 'Oswald Efficiency')
pyl.plot(SetTR, Sete, 'o')


pyl.show()
