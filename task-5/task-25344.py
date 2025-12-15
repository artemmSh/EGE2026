def converter(x, base):
    res = ''
    while x:
        res += str(x % base)
        x //= base
    return res[::-1]


ans = []
for N in range(1, 100_000):
    R = converter(N, 3)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += converter(3 * sum(map(int, R)), 3)
    R = int(R, 3)
    if R > 208 and R % 2:
        ans.append(R)
print(min(ans))
