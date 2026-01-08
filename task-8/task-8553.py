from itertools import *

res = 0
cnt = 0
for pos, val in enumerate(product(sorted('НОРМАЛЬЕ'), repeat=6), start=1):
    val = ''.join(val)

    if val[:4] == 'НОРМ':
        cnt += 1
        if cnt == 1:
            res += pos
    if val == 'НЕНОРМ':
        res -= pos
print(res - 1)
