def f(x):
    res = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            res |= {i, x // i}
    if res:
        return sum(res) // len(res)
    return 0


cnt = 0
for N in range(699_999, 0, -1):
    if f(N) and f(N) % 1000 == 313:
        cnt += 1
        print(N, f(N))
    if cnt == 7:
        break
