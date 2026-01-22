from math import *

for N in range(1, 100_000):
    L = 248
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 75600 * I > 16 * 2 ** 20:
        print(N)
        break
