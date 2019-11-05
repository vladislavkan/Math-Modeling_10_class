import matplotlib.pyplot as plt
import numpy as np
def grafiki(a=1,b=2,c=0,k=1):
    x=np.arange(-2,2,0.1)
    y= a * x ** 2 + b * x + c
    plt.plot( x, y, label='parabola')
    plt.xlabel('coord-x')
    plt.ylabel('coord-y')
    x=np.arange(0.1,10,0.1)
    y1=k/x
    plt.plot( x, y1 , label='giperbola')
    plt.legend()
grafiki()