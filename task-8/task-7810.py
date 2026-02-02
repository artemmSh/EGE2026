from itertools import *

cnt = 0

for val in product('МАСЛО', repeat=6):
    val = ''.join(val)
    if sum(1 for i in val if i in 'АО') == 1:
        cnt += 1
print(cnt)
