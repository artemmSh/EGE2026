from itertools import permutations

cnt = 0
for val in permutations('0123456789', r=4):
    if val[0] != '0':
        val = ''.join('-' if int(i) % 2 else '+' for i in val)
        if '++' not in val and '--' not in val:
            cnt += 1
print(cnt)
