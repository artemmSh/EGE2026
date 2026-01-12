from itertools import permutations

cnt = 0
for val in permutations('012345678', r=7):
    val = ''.join(val)
    if val[0] != '0' and '2' not in val:
        for i in '02468':
            val = val.replace(i, '+')
        for i in '1357':
            val = val.replace(i, '-')
        if '++' not in val and '--' not in val:
            cnt += 1
print(cnt)
