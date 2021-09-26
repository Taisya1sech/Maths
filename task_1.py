%matplotlib inline
import numpy as np

!pip install keyboard

for i in range(0, 5):
    a = input()
    x = np.random.uniform(0, 36)
    if x == 0:
      print("green")
    elif x<18:
        print("red")
    else:
        print("black")
