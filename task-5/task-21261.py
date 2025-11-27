def converter(x, base):
    res = ''
    while x:
        res += str(x % base)
        x //= base
    return res[::-1]


ans = []
for N in range(1, 100_000)[::-1]:
    R = converter(N, 4)
    if not (sum(map(int, R)) % 3):
        R = '32' + R.replace('2', '0')
    else:
        R = R[0] + '10' + R[3:] + '33'
    R = int(R, 4)
    if R == 335:
        print(N)
        break
