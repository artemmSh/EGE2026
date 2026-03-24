from itertools import permutations

cnt = 0
for val in permutations('abicolun', r=8):
    val = ''.join('+' if i in 'aiou' else '-' for i in val)
    if '--' not in val and '++' not in val:
        cnt += 1
print(cnt)
