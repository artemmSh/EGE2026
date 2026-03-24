def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def s(x):
    res = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            if is_prime(i):
                res.append(x)
            if is_prime(x // i):
                res.append(x // i)
    if res:
        return sum(res)
    return 0


cnt = 0
for N in range(250_000, 10 ** 20):
    if s(N) and s(N) % 17 == 0:
        cnt += 1
        print(N, s(N))
    if cnt == 5:
        break
