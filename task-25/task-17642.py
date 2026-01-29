def div(x):
    res = set()
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            if i != 9 and i % 10 == 9:
                res.add(i)
            if (x // i) != 9 and (x // i) % 10 == 9:
                res.add(x // i)
    if len(res) >= 1:
        return min(res)
    return 0


cnt = 0
for N in range(800_000 + 1, 10 ** 20):
    if div(N):
        print(N, div(N))
        cnt += 1
    if cnt == 5:
        break
