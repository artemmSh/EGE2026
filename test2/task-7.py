from math import *

for A in range(100_000, 0, -1):
    i = ceil(log2(4000))
    V = 50 * A * 768 * i
    if V / 1_310_720 <= 300:
        print(A)
        break
