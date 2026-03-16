def converter(x, base):
    res = ''
    while x:
        res += str(x % base)
        x //= base
    return res[::-1]


ans = []
for N in range(1, 100_000):
    R = converter(N, 3)
    if N % 3:
        R = '1' + R + R[-3:]
    else:
        R += converter(sum(map(int, R)) * 8, 3)
    R = int(R, 3)
    ans.append((abs(R - 1220), R))

ans.sort(key=lambda x: (x[0]))
print(ans[0][1])
