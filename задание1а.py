import matplotlib.pyplot as plt
import numpy as np
def clik(R=2, title='cicloida'):
    t = np.arange(-2 * np.pi, 2 * np.pi , 0.1)
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))
    plt.plot(x ,y)
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    plt.legend()
    plt.title()
    plt.show()
clik()