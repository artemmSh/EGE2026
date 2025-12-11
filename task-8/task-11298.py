from itertools import *

cnt = 0
for pos, val in enumerate(product(sorted('АОЖПЮЗ'), repeat=6), start=1):
    val = ''.join(val)
    if (not pos % 2) and val[0] == 'А' and val.count('З') >= 2:
        cnt += 1
print(cnt)
# это уже было решено я комментарий пишу чтобы загитпушить
