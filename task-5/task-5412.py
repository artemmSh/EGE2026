from string import printable as alph


def converter(x, base):
    res = ''
    while x:
        res += alph[x % base]
        x //= base
    return res[::-1]


cnt = 0
for N in range(1, 100_000):
    R = converter(N, 16)
    if R.count('b') % 2 == 0:
        R = '1' + R
    else:
        R += '1'
    R = int(R, 16)
    if 9 < R < 100:
        cnt += 1
print(cnt)
