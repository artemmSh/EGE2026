from itertools import *

cnt = 0
for val in set(permutations('КИДАЛА', r=5)):
    if all(val[i] != val[i + 1] for i in range(len(val) - 1)):
        cnt += 1
print(cnt)
