from math import *
for L in range(1, 100000):
    i = ceil(log2(562))
    I = ceil(L*i/8)
    if 45877*I > 49 * 2 ** 20:
        print(L)
        break