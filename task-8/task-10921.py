from itertools import permutations

cnt = 0
for val in set(permutations('джаваскрипт')):
    val = ''.join(val)
    if sum(i for i, ch in enumerate(val, start=1) if ch in 'аи') == 11:
        cnt += 1
print(cnt)
