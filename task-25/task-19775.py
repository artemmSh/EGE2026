def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def f(x):
    res = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            if is_prime(i): res.add(i)
            if is_prime(x // i): res.add(x // i)
    if res:
        return sum(res)
    return 0


cnt = 0
for N in range(32_500_000 + 1, 10 ** 20):
    if f(N) and f(N) % 145 == 0:
        cnt += 1
        print(N, f(N))
    if cnt == 7:
        break
