from itertools import *
from string import printable as alph

cnt = 0
for val in product(alph[:8], repeat=5):
    val = ''.join(val)
    for i in alph[1:8:2]:
        val = val.replace(i, '*')
    if val[0] != '0' and val.count('6') == 1 and '*6' not in val and '6*' not in val:
        cnt += 1
print(cnt)
