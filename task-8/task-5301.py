from itertools import *

cnt = 0
for val in product('ЛЕСЯ ', repeat=5):
    val = ''.join(val)
    for i in 'ЛС':
        val = val.replace(i, '-')
    for i in 'ЕЯ':
        val = val.replace(i, '+')
    if '--' not in val and '++' not in val and val.count(' ') == 1 and val.index(' ') not in (0, 4):
        cnt += 1
print(cnt)
