def f(x):
    res = set()
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            res |= {i, x // i}
    res_8 = []
    for i in sorted(res):
        if i != 8 and i % 10 == 8:
            res_8 += [i]
    if res_8:
        return min(res_8)
    return 0


cnt = 0
for N in range(500_000 + 1, 10 ** 20):
    if f(N):
        print(N, f(N))
        cnt += 1
    if cnt == 5:
        break
