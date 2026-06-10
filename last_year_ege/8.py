from itertools import *

for pos, val in list(enumerate(product(sorted('строка'), repeat=5), start=1))[::-1]:
    val = ''.join(val)
    if pos % 2 and val[0] not in 'ал' and val.count('с') == 1:
        print(pos)
        break
