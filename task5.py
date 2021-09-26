import numpy as np
import matplotlib.pyplot as plt

def Q(x, y, z):
  return (x**2 + y**2 + z**2)
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = Axes3D(fig)
X = np.arange(-50, 50, 1)
Y = np.arange(-50, 50, 1)
X, Y = np.meshgrid(X, Y)
ax.plot_surface(X, Y, Q(X, 5*X - 14, 21*X - 1))
show()
#plt.plot(x, y, Q(x, 10*x - 14, 21*x - 1))
#plt.xlabel('x')
#plt.ylabel('y')
#plt.grid(True)

A = np.array([[1, 2, -1], [8, -5, 2]])
B = np.array([1, 12])
np.linalg.lstsq(A, B)
