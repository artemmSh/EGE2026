def converter(x, base):
    res = ''
    while x:
        res += str(x % base)
        x //= base
    return res[::-1]


ans = []
for N in range(1, 100_000):
    R = converter(N, 9)
    if R[0] == '7':
        R = R.replace('3', '6')
        R = '34' + R
    else:
        R = '3' + R[1:] + '45'
    R = int(R, 9)
    if R < 2876:
        ans.append([R, N])
ans.sort(key=lambda x: (-x[0], -x[1]))
print(ans[0][1])
