from string import printable as p

ans = set()
for x in range(18):
    for y in range(9 if x < 9 else x + 1, 18):
        num = int(f'5{p[x]}{p[y]}A', 18) + int(f'18{p[x]}7', y)
        ans.add(num)
print(len(ans))
