from math import *

L = 745
N = 10 + 999
i = ceil(log2(N))
I = ceil(L * i / 8)
for dop in range(100_000, 0, -1):
    if 312 * (I + dop) <= 311 * 1024:
        print(dop * 312)
        break
