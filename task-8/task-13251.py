from itertools import *

cnt = 0
for val in permutations('КАЙФ', r=4):
    val = ''.join(val)
    if val[-1] != 'Й' and 'КФ' not in val:
        cnt += 1
print(cnt)
