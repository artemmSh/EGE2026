from math import *

for L in range(100_000, 0, -1):
    N = 10 + 26 + 476
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 5000 * I <= 1 * 2 ** 20:
        print(L)
        break
