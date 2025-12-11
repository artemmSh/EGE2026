from itertools import *

cnt = 0
for val in permutations('ЗАПИСЬ'):
    val = ''.join(val)
    for i in 'АИ':
        val = val.replace(i, '*')
    if val[0] != 'Ь' and '*Ь' not in val: cnt += 1
print(cnt)
