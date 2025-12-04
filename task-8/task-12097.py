from itertools import *

for pos, val in list(enumerate(product(sorted('ГИРЛЯНДА'), repeat=6), start=1))[::-1]:
    val = ''.join(val)
    if (not pos % 2) and val[0] != 'Я' and val.count('Д') == 3:
        print(pos)
        break
