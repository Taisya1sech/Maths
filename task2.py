%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

k,m,l = 0, 0, 0
n = 100
for i in range(0, n):
    x = np.random.uniform(0, 10)
    l=l+1
    if x<5:
        k = k + 1
    else:
        m = m + 1
if k+m==l:
  print(True)
else:
  print(False)
print(k,m,l)

allsums=[]
for i in range(11):
  x=np.random.rand(10)
  allsums.append(sum(x))
  i+=1
num_bins = 10
n, bins, patches = plt.hist(allsums, num_bins)
plt.xlabel('summa')
plt.ylabel('Probability')
plt.title('Histogram')
