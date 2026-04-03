def converter(x, base):
    res = ''
    while x:
        res += str(x % base)
        x //= base
    return res[::-1]


ans = 10 ** 100
for N in range(1, 100_000):
    R = converter(N, 4)
    if N % 4 == 0:
        R += R[-2:]
    else:
        R += converter(4 * (N % 4), 4)
    R = int(R, 4)
    if R > 291:
        ans = min(ans, R)
print(ans)
