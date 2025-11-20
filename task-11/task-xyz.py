from math import *

L = 110
N = 1030
i = ceil(log2(N))
I = ceil(L * i / 8)

print(32768 * I / 1024)
