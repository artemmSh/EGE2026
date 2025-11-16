from string import printable as alph


def converter(x):
    res = ''
    while x:
        res += alph[x % 3]
        x //= 3
    return res[::-1]


ans = []
for N in range(1, 100000):
    R = converter(N)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += converter(sum(map(lambda x: int(x, 36), R)))
    R = int(R, 3)
    if R > 220:
        ans.append(R)
print(min(ans))
