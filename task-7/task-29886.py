from math import *

for a in range(1000000, 0, -1):
    i = ceil(log2(a))
    v = 1024 * 768 * i
    if v == 1536 * 2 ** 13:
        print(a)
        break
