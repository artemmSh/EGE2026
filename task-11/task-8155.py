from math import *

L = 213
N = 1790
i = ceil(log2(N))
I = ceil(L * i / 8)
print(16384 * I / 1024)
