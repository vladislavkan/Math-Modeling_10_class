from constantmodule import g, e, h, k
from math import sqrt, cos, tan, pi
B = 0.52
H = 100
alf = pi/3
v = sqrt(g*H*1/(tan(B))**2/2*(cos(alf))**2*(1-tan(B)*tan(alf)))
print(v)


T = 200
ee = 300
N = 2/sqrt(pi)*h/(k*T)**1.5*e**(-ee/k*T)*ee**(T/2)
print(N)
