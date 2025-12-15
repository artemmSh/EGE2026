from string import printable as alph
from itertools import *

cnt = 0
for val in product(alph[:12], repeat=7):
    val = ''.join(val)
    if val[0] != '0' and val.count('b') == 2:
        for i in alph[:12:2]:
            val = val.replace(i, '+')
        for i in alph[1:12:2]:
            val = val.replace(i, '-')
        if val in '+-+-+-+ -+-+-+-':
            cnt += 1
print(cnt)
