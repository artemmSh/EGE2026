from itertools import *
cnt = 0
for val in product('0123456789', repeat=6):
    if val[0] != '0' and int(''.join(val)) % 4 == 0:
        val = ''.join(['+' for i in val if i in '02468'])
    if all(val.count(i) == 1 for i in val) and '++' not in val:
        cnt += 1
print(cnt)