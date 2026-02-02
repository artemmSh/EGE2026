from math import prod


def is_prime(x):
    if x < 2: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0: return False
    return True


def f(x):
    res = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            if is_prime(i): res += [i]
            if is_prime(x // i): res += [x // i]
    if len(res) == 12 and prod(res) == x:
        return max(res)
    return 0


cnt = 0
for N in range(24_517_512 + 1, 10 ** 20):
    if f(N):
        print(N, f(N))
        cnt += 1
    if cnt == 5:
        break
