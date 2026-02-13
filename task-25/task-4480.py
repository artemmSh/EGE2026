from math import prod


def f(x):
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res |= {i, x // i}
    return res


cnt = 0
for N in range(800_000 + 1, 10 ** 20):
    if len(f(N)) > 10 and prod(f(N)) % 2 and sum(f(N)) % 2:
        cnt += 1
        print(N, len(f(N)))
    if cnt == 6:
        break
