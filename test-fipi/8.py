from itertools import *

for pos, val in enumerate(product(sorted('апрель'), repeat=6), start=1):
    val = ''.join(val)
    if pos % 2 and val[0] not in 'ал' and val.count('п') >= 2:
        print(pos)
        break
