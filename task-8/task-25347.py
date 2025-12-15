from itertools import *

for pos, val in enumerate(product(sorted('ГРАНИТ'), repeat=6), start=1):
    val = ''.join(val)
    if pos % 2 and val[0] not in 'АИГ' and val.count('А') == 1:
        print(pos)
        break
