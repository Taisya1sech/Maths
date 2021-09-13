%matplotlib inline
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

x = np.linspace(-7*np.pi, 2*np.pi, 250)

k, a, b = np.linspace(10,10, num = 3)
k1, a1, b1 = np.linspace(5, 10, num = 3)
k2, a2, b2 = np.linspace(7, 12, num = 3)

print(f'k={k}, a={a}, b={b}')
print(f'k1={k1}, a1={a1}, b1={b1}')
print(f'k2={k2}, a2={a2}, b2={b2}')

plt.figure(figsize = (20, 10))
plt.plot(x, k * np.cos(x - a) + b, label='k, a, b')
plt.plot(x, k1 * np.cos(x - a1) + b1, color='purple', label='k1, a1, b1')
plt.plot(x, k2 * np.sin(x - a2) + b2, color='green', label='k2, a2, b2')

plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend(frameon=False)
plt.show()

