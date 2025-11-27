from math import *

for L in range(1, 100_000):
    N = 10 + 52 + 972
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 2048 * I > 172 * 1024:
        print(L)
        break
