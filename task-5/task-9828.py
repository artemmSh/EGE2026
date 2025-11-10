ans = []


def trio(x):
    res = ''
    while x:
        res += str(x % 3)
        x //= 3
    return res[::-1]


for N in range(1, 1000000):
    R = trio(N)
    if N % 3 == 0:
        R = '1' + R + '02'
    else:
        R += trio(4 * (N % 3))
    R = int(R, 3)
    if R < 199:
        ans.append(N)
print(max(ans))
