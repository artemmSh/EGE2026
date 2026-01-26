ans = 10 ** 10
for N in range(1, 100_000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R += R[-3:]
    else:
        R += bin(3 * (N % 3))[2:]
    R = int(R, 2)
    if R > 151:
        ans = min(ans, R)
print(ans)
