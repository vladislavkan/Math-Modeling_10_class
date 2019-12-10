import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0,4,0.01)

def predprijtie(v,t):
    dvdt = - k*v*t
    return dvdt

v_0 = 1000
k_bact = 0.08

k = k_bact
solve_bact = odeint(predprijtie, v_0, t)

plt.plot(t, solve_bact[:,0])