from math import *

for L in range(1, 100000):
    N = 512
    i = 9
    I = ceil(L*i/8)
    if 345 * I > 70 * 1024:
        print(L)
        break