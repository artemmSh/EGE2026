from math import *

for N in range(1, 10000000000):
    L = 119
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 125_300 * I > 23 * 2 ** 20:
        print(N)
        break
