def f(x):
    res = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            if i not in (11, x) and i % 100 == 11:
                res.append(i)
            if x // i not in (11, x) and (x // i) % 100 == 11:
                res.append(x // i)
    if res:
        return sorted(res)[0]
    return 0


cnt = 0
for n in range(1_350_050 + 1, 10 ** 20):
    if f(n):
        cnt += 1
        print(n, f(n))
    if cnt == 5:
        break
