import matplotlib.pyplot as plt
import numpy as np
def clik(R=4 , title='cicloida'):
    t = np.arange(-2 * np.pi, 2 * np.pi , 0.1)
    x = R * (np.sin(t)) ** 3
    y = R * (np.cos(t)) ** 3
    plt.plot(x ,y)
    plt.xlim(-10,10)
    plt.ylin(-10,10)
    plt.title()
    plt.legend()
    plt.show()
clik()