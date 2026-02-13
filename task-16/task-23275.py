from functools import lru_cache


@lru_cache(None)
def f(n):
    return 2 * (g(n - 3) + 8)


@lru_cache(None)
def g(n):
    if n < 10: return 2 * n
    return g(n - 2) + 1


for i in range(1, 15546):
    g(i)

print(f(15548))
