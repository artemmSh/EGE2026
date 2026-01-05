from math import *

for N in range(1, 100000)[::-1]:
    i = ceil(log2(N) / 8)
    V = 3840 * 2160 * i * 8
    if V / 25600 < 2 * 60 * 60:
        print(N)
        break
