from itertools import *

cnt = 0
for val in set(permutations('СОРТИРОВКА')):
    val = ''.join(val)
    for i in 'ОИА':
        val = val.replace(i, '-')
    for i in 'СРТВК':
        val = val.replace(i, '+')
    if '+++' not in val and '---' not in val:
        cnt += 1
print(cnt)
