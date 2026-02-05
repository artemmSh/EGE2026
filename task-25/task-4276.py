def f(x):
    res = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            res |= {i, x // i}
    if len(res) < 7:
        return 0
    return sorted(res, reverse=True)


cnt = 0
for N in range(400_000_000 + 1, 10 ** 20):
    if f(N):
        cnt += 1
        print(f(N)[6], len(f(N)))
    if cnt == 5:
        break
