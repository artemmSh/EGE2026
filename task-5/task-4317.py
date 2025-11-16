def converter(x, base):
    res = ''
    while x:
        res += str(x % base)
        x //= base
    return res[::-1]


ans = []
for N in range(1, 100_000):
    R = converter(N, 5)
    if not int(R[-1]) % 2:
        R += '2'
    else:
        R = '2' + R + '3'
    R = int(R, 5)
    if R < 1000:
        ans.append(N)
print(max(ans))
