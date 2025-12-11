from itertools import *

cnt = 0
for val in product('КОТБУС', repeat=8):
    val = ''.join(val)
    if 'КОТ' in val and val[0] not in 'ОУ':
        cnt += 1
print(cnt)
