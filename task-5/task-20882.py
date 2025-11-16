def converter(x, base):
    res = ''
    while x:
        res += str(x % base)
        x //= base
    return res[::-1]


for N in range(1, 100_000):
    R = converter(N, 5)
    if len(R) % 2 == 0:
        R = R[len(R) // 2:] + R[:len(R) // 2]
    else:
        R += str(N % 5)
        R = R[len(R) // 2:] + R[:len(R) // 2]
    R = int(R, 5)
    if R > 50:
        print(N)
        break
