from itertools import *

cnt = 0
for pos, val in enumerate(product(sorted('СОЛНЦЕ'), repeat=6), start=1):
    val = ''.join(val)
    if (not pos % 2) and val[0] not in 'ОЕ' and val.count('Ц') == 2:
        cnt += 1
print(cnt)
