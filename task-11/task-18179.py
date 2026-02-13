from math import *

for N in range(1, 100_000):
    L = 20
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 600_000 * I > 11 * 2 ** 20:
        print(N)
        break
