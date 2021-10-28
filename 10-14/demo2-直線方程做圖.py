import numpy as np
import matplotlib.pyplot as plt
from sympy.polys.rings import xring
from sympy.solvers import solve
from sympy import Symbol

def fun1(x):
    return  12 - 5 * x

def fun2(x):
    return  3 - 0.5 * x

x = Symbol('x')

xr = np.linspace(0,12,100)

y1r = fun1(xr)

y2r = fun2(xr)

plt.plot(xr,y1r,'b-')
plt.plot(xr,y2r,'g-')
plt.text(1,8,"y=12-5x",fontsize=12,color="blue")
plt.text(5,1,"y=3-0.5x",fontsize=12,color="green")
plt.xlim(0,12)
plt.ylim(0,12)
plt.show()