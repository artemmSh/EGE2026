def converter(x, base):
    res = ''
    while x:
        res += str(x % base)
        x //= base
    return res[::-1]


ans = []
for N in range(1, 100_000):
    R = converter(N, 7)
    if R[-1] == '2':
        R = R.replace('1', '3')
        R = '21' + R
    else:
        R = '1' + R[1:] + '36'
    R = int(R, 7)
    if R < 744:
        ans.append([R, N])
ans.sort(key=lambda x: (-x[0], x[1]))
print(ans[0][1])
