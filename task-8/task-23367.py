from itertools import *

cnt = 0
for val in product('0123456', repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('6') == 1 and all(val[i] != val[i + 1] for i in range(len(val) - 1)):
        cnt += 1
print(cnt)
