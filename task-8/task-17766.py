from itertools import *

for pos, val in list(enumerate(product(sorted('СЕНТЯБРЬ'), repeat=5), start=1))[::-1]:
    val = ''.join(val)
    if (not pos % 2) and val[0] == 'Р' and 'Ь' not in val:
        print(pos)
        break
