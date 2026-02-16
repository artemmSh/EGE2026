from itertools import *
from math import *

odd = [i for i in range(113, 1_000_000, 113) if i % 2]
power_of_3 = [i for i in range(1, 13)]

cnt = 0
for N in product('123456789', repeat=6):
    N = int(''.join(N))
    for i in odd:
        for j in power_of_3:
            if N == i + 3 ** j:
                cnt += 1
                print(N, j)
    if cnt == 5:
        break
