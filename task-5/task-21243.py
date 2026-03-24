def converter(x, base):
    res = ''
    while x:
        res += str(x % base)
        x //= base
    return res[::-1]


ans = []
for N in range(1, 100_000):
    R = converter(N, 5)
    if sum(map(int, R)) % 5 == 0:
        R = R.replace('1', '0') + '14'
    else:
        R = '44' + R[1:] + '33'
    R = int(R, 5)
    if R > 370:
        ans.append((R, N))

ans.sort(key=lambda x: (x[0], x[1]))
print(ans[0][1])
