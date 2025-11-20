from string import printable as alph

ans = []
for y in range(9, 14):
    for x in range(y + 1, 14):
        N1 = int(f'7{alph[x]}37{alph[y]}', 14)
        N2 = int(f'9{alph[y]}63', x)
        N3 = int(f'15148', y)
        N = N1 + N2 - N3
        ans.append([N, N // (x + y)])
print(max(ans))
