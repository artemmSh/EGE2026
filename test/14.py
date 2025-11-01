def six(x):
    s = ''
    while x > 0:
        s = str(x % 6) + s
        x//=6
    return s

ans = list()
for x in range(1, 2031):
    N = 6 ** 260 + 6 ** 160 + 6 ** 60 - x
    S = six(N)
    if S.count('0') == 202:
        ans.append(x)
print(ans[-1])