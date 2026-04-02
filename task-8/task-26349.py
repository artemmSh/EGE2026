from itertools import *

for l in range(1, 10):
    for pos, val in list(enumerate(product(sorted('сулак'), repeat=l), start=1))[::-1]:
        val = ''.join(val)
        if pos % 2 == 0 and val[0] in 'лс' and sum(i in 'уа' for i in val) <= 2 and sum(val[i] in 'уа' and val[i + 1] in 'уа' for i in range(len(val) - 1)) == 0:
            if pos != 12368:
                break
            else:
                print(l)
                exit()
