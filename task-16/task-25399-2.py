from functools import lru_cache


def f(n):
    if n >= 128: return f(n - 5) + 1092
    return 5 * g(n - 7) + 29


@lru_cache(None)
def g(n):
    if n > 303728: return n - 15
    return g(n + 8) // 2 - 109


for i in range(303728, 0, -1):
    g(i)

print(f(2049))
