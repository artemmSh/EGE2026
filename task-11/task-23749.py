from math import *
for N in range(1, 100_000):
    L = 2783
    i = ceil(log2(N))
    I = ceil(L * i/8)
    if 3845627 * I >= 11 * 2**30:
        print(N)
        break