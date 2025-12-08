from itertools import *
from string import printable as alph

cnt = 0
for val in product(alph[:8], repeat=5):
    if val[0] not in '01357' and val[-1] not in '26' and val.count('7') <= 2:
        cnt += 1
print(cnt)
