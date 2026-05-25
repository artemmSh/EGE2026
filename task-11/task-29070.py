from math import *

for N in range(1, 100_000_000_000):
    i = ceil(log2(N))
    l1 = 7
    l2 = 9
    I1 = ceil(l1 * i / 8)
    I2 = ceil(l2 * i / 8)
    if 384 * I1 + 256 * I2 == 7168:
        print(N)
        break
