from string import printable as alph


def converter(x, base):
    res = ''
    while x:
        res += alph[x % base]
        x //= base
    return res[::-1]


for N in range(1, 1000000):
    R = converter(N, 3)
    if sum(map(lambda x: int(x, 36), R)) % 2 == 0:
        R = '12' + R[2:] + '0'
    else:
        R = '10' + R[2:] + '2'
    R = int(R, 3)
    if R > 105:
        print(N)
        break
