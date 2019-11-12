import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax=plt.subplots()

anim_object, = plt.plot([], [], 'o')

def cicloida_m(r,t):
    x = r * (t - np.sin(t))
    y = r * (1 - np.cos(t))
    return x, y

edge=4
ax.set_xlim(-edge,edge)
ax.set_ylim(-edge,edge)

def animate(i):
    anim_object.set_data(cicloida_m(r=4,t=i))
    
ani=animation.FuncAnimation(fig,
                            animate,
                            frames=np.arange(0,6,0.1),
                            interval=100)

t = np.arange(-2 * np.pi, 2 * np.pi , 0.1)
x = 4 * (t - np.sin(t))
y = 4 * (1 - np.cos(t))
plt.plot(x ,y)

ani.save('cicloida.gif')