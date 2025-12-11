from itertools import *

cnt = 0
for val in permutations('ПРОБНИК', r=7):
    val = ''.join(val)
    for i in 'ПРБНК':
        val = val.replace(i, '-')
    for i in 'ОИ':
        val = val.replace(i, '+')
    if val[0] == '-' and val[-1] == '-' and '++' not in val:
        cnt += 1
print(cnt)
