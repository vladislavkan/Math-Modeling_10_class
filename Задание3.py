import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0,4,0.005)

def jf(t,V):
    dvdt = F/m -(y*V**2)/m
    return dvdt

y = 0.5
F = 10
m = 100
V0 = 0


solve = odeint(jf, V0, t)

plt.plot(t, solve[:,0])