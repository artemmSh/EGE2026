def f(x):
    res = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            res |= {i, x // i}
    if res:
        return sum(res)
    return 0


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


cnt = 0
for N in range(1_273_547 + 1, 10 ** 20):
    if is_prime(f(N) % 100_000) and sum(map(int, str(N))):
        cnt += 1
        print(N, f(N))
    if cnt == 5:
        break
