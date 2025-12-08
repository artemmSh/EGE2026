from string import printable as alph
from itertools import *

cnt = 0
for val in permutations(alph[:16], r=3):
    val = ''.join(val)
    if val[0] != '0':
        for i in alph[:16:2]:
            val = val.replace(i, '+')
        for i in alph[1:16:2]:
            val = val.replace(i, '-')
        if '--' not in val and '++' not in val:
            cnt += 1
print(cnt)
