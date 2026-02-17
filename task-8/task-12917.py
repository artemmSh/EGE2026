from itertools import permutations

cnt = 0
for val in set(permutations('prosto')):
    val = ''.join(val)
    if all(val[i] != val[i + 1] for i in range(len(val) - 1)):
        cnt += 1
print(cnt)
