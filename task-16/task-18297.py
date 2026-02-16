from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 10: return n - 1
    elif n % 2: return 5 * n + 2 + f(n - 4)
    return 3 * n - 1  + f(n - 3)

for i in range(1, 4500):
    f(i)

print(f(4445) - f(4444))