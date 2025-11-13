def converter(x):
    res = ''
    while x:
        res += str(x % 7)
        x //= 7
    return res[::-1]


ans = []
for N in range(1, 1000000):
    R = converter(N)
    if sum(map(int, R)) % 2 == 0:
        R += '555'
    else:
        R = '33' + R + '6'
    R = int(R, 7)
    if R < 12717:
        ans.append(N)
print(max(ans))
