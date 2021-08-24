%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 155)
plt.plot(x, np.cos(x), marker = "o")
plt.plot(x, np.cos(2*x), marker = "o")
