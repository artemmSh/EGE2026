def converter(x, base):
    res = ''
    while x:
        res += str(x % base)
        x //= base
    return res[::-1]


ans = 100 ** 100
for n in range(1, 100_000):
    r = converter(n, 3)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += converter(5 * (n % 3), 3)
    r = int(r, 3)
    if r > 150:
        ans = min(ans, r)
print(ans)
