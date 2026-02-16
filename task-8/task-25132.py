from itertools import *

summa = 0
for pos, val in enumerate(product(sorted('СДАЙЕГЭ'), repeat=6), start=1):
    val = ''.join(val)
    if 'ЕГЭ' in val:
        summa += pos
print(summa)
