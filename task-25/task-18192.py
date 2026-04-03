def is_prime(x):
    if x < 2: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def f(x):
    res = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            if is_prime(i):
                res.append(i)
            if is_prime(x // i):
                res.append(x // i)
    if len(res) == 3:
        return max(res)
    return False


cnt = 0
for N in range(1_000_000 + 1, 10 ** 20):
    if f(N):
        cnt += 1
        print(N, f(N))
    if cnt == 5:
        break
