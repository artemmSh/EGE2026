def is_prime(x):
    if x < 2: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0: return False
    return True


def f(x):
    res = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            if is_prime(i): res.append(i)
            if is_prime(x // i): res.append(x // i)
    if len(res) >= 2:
        return max(res) + min(res)
    return 0


cnt = 0
for n in range(23_600_000 + 1, 10 ** 30):
    if f(n) % 213 == 171:
        cnt += 1
        print(n, f(n))
    if cnt == 6:
        break
