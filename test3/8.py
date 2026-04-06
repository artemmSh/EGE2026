from itertools import *
from string import printable as alph

cnt = 0
for val in product(alph[:7], repeat=7):
    val = ''.join(val)
    if val[0] not in '035' and not ('22' in val and '44' in val):
        cnt += 1
print(cnt)
