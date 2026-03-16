from itertools import *

cnt = 0

for val in product('0123456', repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        for i in '0246':
            val = val.replace(i, '*')
        if '***' not in val and sum(val[i:i + 2] == '**' for i in range(len(val) - 1)) >= 2:
            cnt += 1
print(cnt)
