from itertools import *
from string import printable as alph

cnt = 0
for val in product(alph[:15], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('8') == 1 and sum(val.count(i) for i in alph[10:15]) >= 2:
        cnt += 1
print(cnt)
