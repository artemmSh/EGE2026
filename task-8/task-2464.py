from itertools import *

cnt = 0
for val in product('НИЧЬЯ', repeat=7):
    val = ''.join(val)
    val = val.replace('И', '*').replace('Я', '*')
    if val.count('*') == 2 and '**' not in val:
        cnt += 1
print(cnt)
