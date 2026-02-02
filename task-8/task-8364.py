from itertools import *

pos1 = 0
pos2 = 0
for pos, val in (enumerate(product(sorted('КРАТЕ'), repeat=6), start=1)):
    val = ''.join(val)
    if val == 'КАРЕТА':
        pos1 = pos
    if val == 'РАКЕТА':
        pos2 = pos
print(abs(pos2 - pos1) - 1)
