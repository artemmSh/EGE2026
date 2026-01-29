from itertools import *

for pos, val in enumerate(product(sorted('АЕКНС'), repeat=6), start=1):
    if ''.join(val) == 'СЕНЕКА':
        print(pos)
