from itertools import *

for pos, val in enumerate(product(sorted('АВТОР'), repeat=4), start=1):
    val = ''.join(val)
    if val == 'ВАТА':
        print(pos)
