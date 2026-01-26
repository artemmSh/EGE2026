from itertools import *
from string import printable as alph

cnt = 0
for val in product(alph[:9], repeat=7):
    if val[0] != '0' and val.count('8') == 1 and val[0] not in alph[1:9:2] and val[-1] not in alph[:9:2]:
        cnt += 1
print(cnt)
