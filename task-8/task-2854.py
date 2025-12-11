from itertools import *

cnt = 0
for val in set(permutations('РОСОМАХА', r=8)):
    val = ''.join(val)
    if all(val.count(i) == 'РОСОМАХА'.count(i) for i in val):
        for i in 'РСМХ':
            val = val.replace(i, '+')
        for i in 'ОА':
            val = val.replace(i, '-')
        if '++' not in val and '--' not in val:
            cnt += 1
print(cnt)
