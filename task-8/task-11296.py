from itertools import *

for pos, val in enumerate(product(sorted('ДОСЖ'), repeat=6), start=1):
    val = ''.join(val)
    if val[:2] == 'ЖС':
        print(pos)
        break
