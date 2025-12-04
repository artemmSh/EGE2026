from itertools import *

cnt = 0
for val in product('ПИТОН', repeat=4):
    val = ''.join(val)
    val = val.replace('П', '+').replace('Т', '+').replace('Н', '+').replace('И', '*').replace('О', '*')
    if '++' not in val and '**' not in val:
        cnt += 1
print(cnt)
