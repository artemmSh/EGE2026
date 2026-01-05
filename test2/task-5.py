def converter(x, base):
    res = ''
    while x:
        res += str(x % base)
        x //= base
    return res[::-1]


ans = 10 ** 10
for N in range(1, 100_000):
    R = converter(N, 3)
    if sum(map(int, R)) % 2 == 0:
        R = '1' + R + '2'
    else:
        R = '2' + R + '0'
    R = int(R, 3)
    if R > 100:
        ans = min(ans, R)
print(ans)
