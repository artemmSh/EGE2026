from itertools import *

for pos, val in list(enumerate(product(sorted(set('СУБЛИМАЦИЯ')), repeat=5), start=1))[::-1]:
    val = ''.join(val)
    if pos % 2 and val[-1] != 'Я' and sum(1 for i in val if i in 'УИАЯ') == 2:
        print(pos)
        break
