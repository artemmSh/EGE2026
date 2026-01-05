from itertools import *

for pos, val in enumerate(product(sorted('ШКОЛА'), repeat=5), start=1):
    val = ''.join(val)
    if val == 'ШАЛАШ':
        print(pos)
