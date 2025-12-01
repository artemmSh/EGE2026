from itertools import *

for pos, val in enumerate(product(sorted('АЛГОРИТМ'), repeat=5), start=1):
    val = ''.join(val)
    if (not pos % 2) and val[0] not in 'АГ' and val.count('Р') >= 2:
        print(pos, val)
        break

