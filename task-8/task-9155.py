from itertools import *

cnt = 0
for pos, val in enumerate(product(sorted('АПРЕЛЬ', reverse=True), repeat=5), start=1):
    val = ''.join(val)
    if val[-1] == 'Ь':
        cnt += 1
    if pos == 387:
        break
print(cnt)
