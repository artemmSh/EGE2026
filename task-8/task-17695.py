from itertools import *
from string import printable as alph

cnt = 0
for val in product(alph[:7], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and sum(3 <= int(i) <= 5 for i in val) == 2 and all(val[i] != val[i + 1] for i in range(len(val) - 1)):
        cnt += 1
print(cnt)
