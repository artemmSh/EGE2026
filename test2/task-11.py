from math import *

for N in range(1, 1000_000):
    L = 278
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 38045 * I >= 11 * 1024 * 1024:
        print(N)
        break
