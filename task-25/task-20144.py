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
            if is_prime(i):
                res.add(i)
            if is_prime(x // i):
                res.add(x // i)
    if len(res) > 1:
        return max(res) - min(res)
    return 0


cnt = 0
for N in range(3_333_337 + 1, 10 ** 100):
    if f(N) > 1000 and f(N) % 3 == 0:
        cnt += 1
        print(N, f(N))
    if cnt == 5:
        break
