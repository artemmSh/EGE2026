from itertools import *

cnt = 0
for val in product('АЛГОРИТМ', repeat=6):
    val = ''.join(val)
    if (val.count('Л') <= 1) and (val[0] != 'Р') and (val[-1] not in 'ЛГРТМ'):
        cnt += 1
print(cnt)
