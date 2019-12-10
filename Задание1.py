import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0,200,1)

def razmnojenie(n,t):
    dndt = k*n
    return dndt

n_0 = 1
k_bact = 0.02

k = k_bact
solve_bact = odeint(razmnojenie, n_0, t)

plt.plot(t, solve_bact[:,0],label ='Размножение')