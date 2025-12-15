from itertools import *

for pos, val in list(enumerate(product(sorted('БМЮРН'), repeat=6), start=1))[::-1]:
    val = ''.join(val)
    if pos % 2 and val[0] != 'М' and val.count('Р') >= 2 and 'Ю' not in val:
        print(pos)
        break
