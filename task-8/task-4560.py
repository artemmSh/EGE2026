from itertools import permutations, repeat

cnt = 0
for val in permutations('ТИХОРЕЦК', r=4):
    val = ''.join(val)
    if sum(1 for i in range(4) if val[i] == 'ТИХО'[i]) == 2:
        for i in 'ИОЕ':
            val = val.replace(i, '*')
    if val.count('*') == 2:
        cnt += 1
print(cnt)
