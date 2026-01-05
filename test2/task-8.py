from itertools import *
from string import printable as alph

cnt = 0
for val in product(alph[:25], repeat=4):
    val = ''.join(val)
    if val[0] != '0' and sum(1 for i in val if int(i, 25) % 2) == 1 and sum(1 for i in val if int(i, 25) <= 5) <= 2:
        cnt += 1
print(cnt)
