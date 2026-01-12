from itertools import permutations

cnt = 0
for val in set(permutations('Х*Ч*Н*Б*ДЖ*Т.')):
    val = ''.join(val)
    if '*' * 5 not in val:
        cnt += 1
print(cnt)
