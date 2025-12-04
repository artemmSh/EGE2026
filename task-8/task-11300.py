from itertools import *

for pos, val in list(enumerate(product(sorted('ГОНДУБШ'), repeat=6), start=1))[::-1]:
    val = ''.join(val)
    if (pos % 2) and val[0] != 'Б' and val.count('Н') >= 2 and 'У' not in val:
        print(pos)
        break
