import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def diff(z,t):
    s,v = z
    ds_dt = v
    dv_dt = -9.8*np.sin(s/l)
    return ds_dt, dv_dt



s0 = 1.5
v0 = 1
l = 1
z0 = s0 , v0
solve = odeint(diff, z0, t)

plt.plot(solve[:,0],'g', label='hgduohi')
plt.legend()
plt.show()