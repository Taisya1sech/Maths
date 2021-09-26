import numpy as np
import itertools

for p in itertools.product("0123", repeat=4):
    print(''.join(p))
