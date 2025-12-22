from itertools import *

cnt = 0
for val in product('0123456', repeat=6):
    val = ''.join(val)
    if val[0] != '0' and val[-1] not in '0123' and sum(1 for i in val if int(i) % 2) == 3:
        cnt += 1
print(cnt)