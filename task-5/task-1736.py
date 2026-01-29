ans = 10 ** 10
for N in range(1, 100_000):
    R = bin(N)[2:]
    for i in '01':
        R = R.replace(i, 2 * i)
    R = int(R, 2)
    if R > 63:
        ans = min(ans, R)
print(ans)
