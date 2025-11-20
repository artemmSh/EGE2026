def converter(x, base):
    res = ''
    while x:
        res += str(x % base)
        x //= base
    return res[::-1]


ans = []
for N in range(1, 1_00_000):
    R = converter(N, 3)
    if sum(map(int, R)) % 3 == 0:
        R += '212'
    else:
        R += converter(sum(map(int, R)) * 2, 3)
    R = int(R, 3)
    if R > 490:
        ans.append(R)
print(min(ans))
