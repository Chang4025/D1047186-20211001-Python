import numpy as np
import matplotlib.pyplot as plt
from sympy.polys.rings import xring
from sympy.solvers import solve
from sympy import Symbol

def fun1(x):
    return 12 - 5 * x

x = Symbol('x')

xr = np.linspace(0,12,100)

y1r = fun1(xr)

plt.plot(xr,y1r,'b-')

plt.xlim(0,12)
plt.ylim(0,12)
plt.show()