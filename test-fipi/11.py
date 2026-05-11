from math import *

L = 257
N = 17 + 4080
i = ceil(log2(N))
I = ceil(L * i / 8)
print(8_388_608 * I / 2 ** 20)
