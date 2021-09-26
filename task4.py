import numpy as np
import intertools
import sys
import math

k, n = 0, 1000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(0, n):
    if x[i] == 2:
        k = k + 1
v=(0.5**k)*(0.5**(n-k))
#print(a, b, c, d)
#print(x)
print(k, n, k/n,v)
