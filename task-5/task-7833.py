def converter(x):
    res = ''
    while x:
        res += str(x % 3)
        x //= 3
    return res[::-1]


ans = []
minimum = 100000000000000000000000
for N in range(1, 1_000_000):
    R = converter(N)
    if N % 2 == 0:
        R += R[-2:]
    else:
        R += converter(sum(map(int, R)))
    R = int(R, 3)
    if N > 9:
        if R < minimum:
            minimum = R
            print(R, N)
            # ans.append(N)
print(ans)
