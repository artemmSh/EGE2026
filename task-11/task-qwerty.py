from math import *

ans = []
for N in range(1, 1000000):
    L = 23
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 500_000 * I <= 21 * 2 ** 20:
        ans.append(N)
print(ans[-1])
