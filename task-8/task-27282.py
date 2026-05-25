from itertools import *
from string import printable as alph

cnt = 0
for val in product(alph[:13], repeat=6):
    val = ''.join(val)
    if val[0] != '0' and val.count('0') >= 2:
        val = ''.join('*' if int(i, 13) > 9 else i for i in val)
        if val.count('*') == 2 and '**' in val:
            cnt += 1
print(cnt)
