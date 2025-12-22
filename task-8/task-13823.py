from itertools import *

for pos, val in list(enumerate(product(sorted('МИЗАНТРОП'), repeat=5), start=1))[::-1]:
    val = ''.join(val)
    if pos % 2 == 0 and val[0] == 'Н' and val.count('Р') == 2:
       print(pos)
       break