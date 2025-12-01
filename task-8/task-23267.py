from itertools import *

for pos, val in enumerate(product(sorted('СТРОКА'), repeat=5), start=1):
    val = ''.join(val)
    if pos % 2 and val[0] not in 'АЛ' and val.count('С') == 1:
        print(pos, val)
