import matplotlib.pyplot as plt
import numpy as np
def grafiki(R=1,a=2,b=1):
    x=np.arange(-2*a,2*a,0.01)
    y=np.arange(-2*a,2*a,0.01)
    X,Y= np.meshgrid(x,y)
    fxy= X ** 2 + Y ** 2
    plt.contour(X,Y, fxy, levels=[R**2])
    plt.xlabel('coord-x')
    plt.ylabel('coord-y')
    X,Y= np.meshgrid(x,y)
    fxy1=(X**2/a**2)+(Y**2/b**2)
    plt.contour(X,Y, fxy1,levels=[1])
    plt.legend()
grafiki()