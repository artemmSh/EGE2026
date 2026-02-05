def f(x):
    res = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            res |= {i, x // i}
    if len(res) > 1:
        return min(res) + max(res)
    return 0


cnt = 0
for N in range(800_000 + 1, 10 ** 20):
    if f(N) and f(N) % 10 == 4:
        cnt += 1
        print(N, f(N))
    if cnt == 5:
        break
