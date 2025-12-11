from math import *

for N in range(1, 100_000_0):
    # L1 = 10
    # L2 = 25
    L = 35
    i = ceil(log2(N))
    I = ceil(L * i / 8) + 48
    # I2 = ceil(L2 * i / 8)
    if 1536 * I == 120 * 1024:
        print(N)
