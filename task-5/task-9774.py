ans = []


def trio(x):
    res = ''
    while x:
        res += str(x % 3)
        x //= 3
    return res[::-1]


for N in range(1, 100000):
    R = trio(N)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += trio((N % 3) * 5)
    R = int(R, 3)
    if R > 133:
        ans.append(R)
print(min(ans))
