def f(x):
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res |= {i, x // i}
    return sum(res)


for N in range(1000, 10000):
    if f(N) and f(N) % 100 == 23:
        print(N, f(N))
