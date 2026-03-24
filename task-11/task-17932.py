from math import *

for N in range(10 ** 6, 0, -1):
    L = 211
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 23_654 * I <= 3241 * 2 ** 10:
        print(N)
        break
