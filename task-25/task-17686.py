def div(x):
    res = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0 and i % 10 == 7 and i != 7:
            res.add(i)
        if x % (x // i) == 0 and (x // i) % 10 == 7 and (x // i) != 7:
            res.add(x // i)
    return sorted(res)


cnt = 0
for N in range(700_000 + 1, 10 ** 20):
    if div(N):
        cnt += 1
        print(N, div(N)[0])
    if cnt == 5:
        break
