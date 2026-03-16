from itertools import *

for pos, val in list(enumerate(product(sorted('argument'), repeat=4), start=1))[::-1]:
    val = ''.join(val)
    if len(val) == len(set(val)) and ''.join(sorted(val)) == val:
        print(pos)
        break
