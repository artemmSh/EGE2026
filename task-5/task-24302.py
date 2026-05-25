def converter(x, base):
    res = ''
    while x:
        res += str(x % base)
        x //= base
    return res[::-1]


ans = 100 ** 100
for n in range(1, 100_000):
    r = converter(n, 3)
    if sum(map(int, r)) % 9 == 0:
        r += '2'
    else:
        r += converter((sum(map(int, r)) % 9), 3)
    r = int(r, 3)
    if n > 166:
        ans = min(ans, r)

print(ans)
