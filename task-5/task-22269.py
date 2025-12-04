def converter(x, base):
    res = ''
    while x:
        res += str(x % base)
        x //= base
    return res[::-1]

ans = []
for N in range(1, 100_000):
    R = converter(N, 5)
    if R[-1] == '0':
        R = '33' + R.replace('4', '1')
    else:
        R = '3' + R[1:] + '42'
    R = int(R, 5)
    if R < 1922:
        ans.append([R, N])
ans.sort(key=lambda x: (-x[0], x[0]))
print(ans[0][1])