def converter(x, base):
    res = ''
    while x:
        res += str(x % base)
        x //= base
    return res[::-1]


for N in range(100_000, 0, -1):
    R = converter(N, 3)
    if N % 3:
        R += converter(4 * (N % 3), 3)
    else:
        R = '1' + R + '02'
    R = int(R, 3)
    if R < 100:
        print(N)
        break
