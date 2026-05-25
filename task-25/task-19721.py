def f(x):
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)
    if len(res) == 4:
        return sorted(res, reverse=True)
    return 0


for i in range(178965, 178983):
    if f(i):
        print(*f(i))
