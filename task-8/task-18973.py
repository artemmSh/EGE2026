from itertools import *
from string import printable as alph

cnt = 0
for val in product(alph[:25], repeat=4):
    val = ''.join(val)
    if val[0] != '0' and any(int(i, 36) % 2 == 0 for i in val) and sum(int(i, 36) > 15 for i in val) > 2:
        cnt += 1
print(cnt)
