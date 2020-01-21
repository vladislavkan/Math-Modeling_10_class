import numpy as np
from scipy.integrate inport odient
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

t = np.arange(10**(-7),1.1*10**(-7),10**(-11))

def move_func(s,t):
    x, v_x, y, v_y, z, v_z = s
    dxdt = v_x
    dv_xdt = q / m * (Ex + v_y * By *v_z)
    dydt = v_y
    dv_ydt = q / m * (Ey + v_z * Bx - Bz * v_x)
    dzdt = v_z
    dv_zdt = q / m * (Ez + v_x)