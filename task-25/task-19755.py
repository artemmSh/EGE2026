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
    if len(res) > 1:
        return min(res) + max(res)
    return 0


cnt = 0
for N in range(1_200_000 + 1, 10 ** 20):
    if f(N) > 2000 and f(N) % 10 == 8:
        cnt += 1
        print(N, f(N))
    if cnt == 5:
        break
