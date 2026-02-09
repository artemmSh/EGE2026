from math import *

for L in range(1000000, 0, -1):
    N = 10 + 52 + 1989
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 836 * I <= 639 * 2 ** 10:
        print(L)
        break
