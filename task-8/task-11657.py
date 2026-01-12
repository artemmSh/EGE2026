from itertools import *

cnt = 0

for val in permutations('01234567', r=6):
    val = ''.join(val)
    if val[0] != '0' and '3' not in val:
        for i in '0246':
            val = val.replace(i, '*')
        if '**' in val:
            cnt += 1
print(cnt)
