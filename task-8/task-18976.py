from itertools import *
from string import printable as alph

cnt = 0
for val in product(alph[:20], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and (int(val[0], 36) + int(val[-1], 36) == 26):
        for i in alph[:20:2]:
            val = val.replace(i, '+')
        for i in alph[1:20:2]:
            val = val.replace(i, '-')
        if all(val[i] != val[i+1] for i in range(len(val)-1)):
            cnt += 1
print(cnt)
