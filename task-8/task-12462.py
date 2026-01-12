from itertools import *
from string import printable as alph

cnt = 0
for r in (3, 5):
    for val in permutations(alph[:16], r=r):
        val = ''.join(val)
        if val[0] != '0' and all(int(val[i], 16) > int(val[i + 1], 16) for i in range(len(val) - 1)):
            cnt += 1
print(cnt)
