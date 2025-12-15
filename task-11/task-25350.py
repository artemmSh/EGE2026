from math import *

for N in range(1, 100_000_0):
    L = 105
    i = ceil(log2(N))
    I = ceil(L*i/8)
    if 65536*I >= 7*2**20:
        print(N)
        break