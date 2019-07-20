import math

def solverho(h):
    """
    This function is used to determine the air density (rho)
    provided the altitude in feet.
    """
    temp = 59 - 0.00356 * h
    press = 2116 * ((temp + 459.7) / 518.6) ** 5.256
    rho = press / (1718 * (temp + 459.7))

    return rho

# This section of code determines power loading.
Vmax = int(input("Enter desired maximum velocity in knots:"))
Whp = 680 * Vmax ** -0.79               # Weight to HP ratio smooth, retractable

# This section of code determines wing loading.
Vstall = int(input("Enter desired stall velocity in knots:"))

h = 0                       # Represents sea level
rho = solverho(h)
qstall = 0.5 * rho * ((Vstall * 1.689) ** 2) # dynamic pressure
Clmax = 1.5                 # maximum lift coefficient
WS = qstall * Clmax         # Weight to Wing area ratio

# This section of code determines airplane sizing.

SwetSref = 3.8              # Single engine Conventional design

Cfe = 0.005                 # Single engine, retractable gear, smooth design
Cd0 = Cfe * SwetSref
A = 8
#A = float(input("Enter Aspect Ratio:"))         # Aspect ratio
K = 0.424 / A               # Drag due to lift factor
Vcruise = 155
#Vcruise = int(input("Enter cruise velocity (kts):"))  # desired cruise velocity
Vcr = Vcruise * 1.689
h = 9000
#h = float(input("Enter cruise altitude in feet:"))
rho = solverho(h)           # air density @ 9000 ft, slugs/ft^3
qcruise = 0.5 * rho * (Vcr ** 2) # dynamic pressure
LD = 1/ ((qcruise * Cd0 / (WS * 0.98)) + ((WS * 0.98) * K / qcruise))

cbhp = 0.5 / 3600 # SFC lbs/hr/hp to lbs/sec/hp

np = 0.75 # propeller efficiency
Range = Vcruise * 4 * 6076 # 4 hour cruise range in feet
WfW0 = (1 - 0.975 * 2.7183 ** -((Range * cbhp) / (550 * np * LD))) * 1.06

a = 1.15 # Composite Single Engine

for W0g in range(250, 3000):
    WeW0 = a * W0g ** -0.09
    W0 = 500 / (1 - WeW0 - WfW0)
    if W0 - W0g < 1:
        break

HP = W0 / Whp

D3 = 1.50 * HP ** 0.25
n = 2700 / 60
Vtip = math.sqrt((Vcr ** 2) + (math.pi * n * D3)**2)

S = W0 / WS
b = math.sqrt(A * S)

lamda = 0.6
Croot = (2 * S) / (b * (1 + lamda))
Ctip = lamda * Croot
MAC = (2 / 3) * Croot * ((1 + lamda + lamda ** 2) / (1 + lamda))

Ccr = WS / qcruise

alpha = Ccr * (10 + 18 / A) + -4.2


print("W/hp:", Whp)
print("W/S:", WS)
print("Lift/Drag", LD)
print("Range:", Range)
print("Wf/W0:", WfW0)
print("W0:", W0)
print("HP:", HP)
print("Propeller Diameter:", D3)
print("Tip Speed:", Vtip)
print("Wing Area (ft^2):", S)
print("Wing Span (ft):", b)
print("Root Chord:", Croot)
print("Tip Chord:", Ctip)
print("Mean Aerodynamic Chord:", MAC)
print("coefficient of lift (cruise):", Ccr)
print("Alpha incidence angle:", alpha)

# NASA/Langley LS(1)-0413 Airfoil co-ordinates
AFx = [0.0000, 0.0020, 0.0050, 0.0125, 0.0250, 0.0375, 0.0500, 0.0750, \
0.1000, 0.1250, 0.1500, 0.1750, 0.2000, 0.2250, 0.2500, 0.2750, 0.3000, \
0.3250, 0.3500, 0.3750, 0.4000, 0.4250, 0.4500, 0.4750, 0.5000, 0.5250, \
0.5500, 0.5750, 0.6000, 0.6250, 0.6500, 0.6750, 0.7000, 0.7250, 0.7500, \
0.7750, 0.8000, 0.8250, 0.8500, 0.8750, 0.9000, 0.9250, 0.9500, 0.9750, \
1.0000, 0.00000, .00200, .00500, .01250, .02500, .03750, .05000, .07500, \
0.10000, .12500, .15000, .17500, .20000, .22500, .25000, .27500, .30000, \
0.32500, .35000, .37500, .40000, .42500, .45000, .47500, .50000, .52500, \
0.55000, .57500, .60000, .62500, .65000, .67500, .70000, .72500, .75000, \
0.77500, .80000, .82500, .85000, .87500, .90000, .92500, .95000, .97500, \
1.00000]

AFy = [0.0000, 0.0104, 0.0159, 0.0242, 0.0332, 0.0397, 0.0448, 0.0526, \
0.0586, 0.0635, 0.0675, 0.0710, 0.0740, 0.0765, 0.0786, 0.0803, 0.0818, \
0.0830, 0.0838, 0.0843, 0.0846, 0.0846, 0.0844, 0.0838, 0.0829, 0.0817, \
0.0802, 0.0783, 0.0761, 0.0733, 0.0702, 0.0667, 0.0629, 0.0587, 0.0542, \
0.0495, 0.0445, 0.0393, 0.0340, 0.0284, 0.0227, 0.0169, 0.0110, 0.0048, \
-0.0016, 0.0000, -.0050, -.0094, -.0145, -.0191, -.0223, -.0250, -.0294, \
-.03280, -.03560, -.03790, -.03980, -.04140, -.04270, -.04370, -.04430, \
-.04480, -.04510, -.04520, -.04500, -.04470, -.04420, -.04350, -.04260, \
-.04140, -.03990, -.03810, -.03590, -.03330, -.03050, -.02740, -.02420, \
-.02100, -.01770, -.01440, -.01130, -.00830, -.00570, -.00350, -.00180, \
-.00080, -.00060, -.00130, -.00340, -.00710]
