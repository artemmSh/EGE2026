from itertools import *

cnt = 0
for val in product('ПОЛИНА', repeat=8):
    val = ''.join(val)
    for i in 'ОИА':
        val = val.replace(i, '+')
    for i in 'ПЛН':
        val = val.replace(i, '-')
    if val.count('-') > val.count('+'):
        cnt += 1
print(cnt)