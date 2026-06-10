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
    if len(res) >= 2:
        return min(res) + max(res)
    return 0


cnt = 0
for n in range(5_400_001, 100 ** 100):
    if f(n) > 60_000 and str(f(n)) == str(f(n))[::-1]:
        cnt += 1
        print(n, f(n))
    if cnt == 5:
        break
