  
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation


t = np.arange(10**(-7), 1.1*10**(-7),10**(-11))

def func(s, t):
    (x1, vx1, y1, vy1,
     x2, vx2, y2, vy2,
     x3, vx3, y3, vy3) = s
    dxdt1 = vx1
    dvxdt1 = (k * q1 * q2 / m1 * (x1 - x2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
    + k *q1 * q3 / m1 * (x1 - x3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5)
   
    dydt1 = vy1
    dvydt1 = (k * q1 * q2 / m1 * (y1 - y2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
    + k *q1 * q3 / m1 * (y1 - y3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5)
   
    
    dxdt2 = vx2
    dvxdt2 = (k * q2 * q1 / m2 * (x2 - x1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
    + k *q2 * q3 / m2 * (x2 - x3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5)
   
    
    dydt2 = vy2
    dvydt2 = (k * q2 * q1 / m2 * (y2 - y1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
    + k *q2 * q3 / m2 * (y2 - y3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5)
   
    
    dxdt3 = vx3
    dvxdt3 = (k * q3 * q1 / m3 * (x3 - x1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
    + k *q3 * q2 / m3 * (x3 - x2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5)
   
    
    dydt3 = vy3
    dvydt3 = (k * q3 * q1 / m3 * (y3 - y1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
    + k *q3 * q2 / m3 * (y3 - y2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5)
   
    
    return (dxdt1, dvxdt1, dydt1, dvydt1,
            dxdt2, dvxdt2, dydt2, dvydt2,
            dxdt3, dvxdt3, dydt3, dvydt3)
    
    



k = 8.98755 * 10**9

x10 = -0.008
vx10 = 0
y10 = 0   
vy10 = - 2*10**6
    
x20 = 0.008
vx20 = 0
y20 = 0   
vy20 = 3* 10**6
    
x30 = 0
vx30 = -4*10**6
y30 = 0.01386
vy30 = 0
    
s0 = (x10, vx10, y10, vy10,
      x20, vx20, y20, vy20,
      x30, vx30, y30, vy30)


m1 = 1.7 * 10**(-31)
q1 = 1.1 * 10**(-14)

m2 = 1.8 * 10**(-31)
q2 = 1.2 * 10**(-14)

m3 = 1.5 * 10**(-31)
q3 = -1.1 * 10**(-14)


sol = odeint(func, s0, t)


fig = plt.figure()
bodys = []

for i in range (0, len(t), 1):
    body1, = plt.plot(sol[:i, 0], sol[:i, 2], '-', color ='r')
    body1_line, = plt.plot(sol[i, 0], sol[i, 2], 'o', color = 'r')
    
    body2, = plt.plot(sol[:i,4], sol[:i,6], '-', color ='g')
    body2_line, = plt.plot(sol[i,4], sol[i, 6], 'o', color = 'g')
     
    body3, = plt.plot(sol[:i,8], sol[:i,10], '-', color ='b') 
    body3_line, = plt.plot(sol[i,8], sol[i,10], 'o', color = 'b')
    
    bodys.append([body1, body1_line, body2, body2_line, body3, body3_line])
    
ani = ArtistAnimation(fig, bodys, interval=50)
plt.axis('equal')
ani.save('CgmjhFinal.gif')