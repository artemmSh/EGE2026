from itertools import *

cnt = 0
for i in range(5, 8):
    for val in product('БЕРСК', repeat=i):
        cnt += 1
print(cnt)
