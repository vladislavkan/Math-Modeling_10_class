import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import numpy as np
 
fig = plt.figure()
ax = p3.Axes3D(fig)
 
phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, 5*np.pi, 100)

a = 10
b = 20
c = 30 
h = 20
l = 3
m = 30


x = np.outer(phi , np.cos(theta)) + l * theta**2
y = np.outer(phi , np.sin(theta)) + m * theta**2
z = h*np.outer(np.ones(np.size(theta)), theta)
ax.plot_surface(x, y, z, color='r')
plt.show()