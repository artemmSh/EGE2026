from itertools import *

cnt = 0
for val in product(set('ДИОНИСИЙ'), repeat=6):
    val = ''.join(val)
    if ('Д' in val) ^ ('Н' in val):
        if all(val[i] != val[i + 1] for i in range(len(val) - 1)):
            cnt += 1
print(cnt)
