from itertools import *

cnt = 0

for val in set(permutations('ПАРИЖАНКА')):
    val = ''.join(val)
    for i in 'АИ':
        val = val.replace(i, '*')
    if sum(1 for i in range(len(val) - 1) if val[i] == val[i + 1] == '*') == 1:
        cnt += 1
print(cnt)
