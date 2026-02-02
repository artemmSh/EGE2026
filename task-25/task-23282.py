def is_prime(x):
    if x < 2: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def f(x):
    res = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            if is_prime(i): res |= {i}
            if is_prime(x // i): res |= {x // i}
    if len(res) > 1:
        M = max(res) + min(res)
        if M > 60_000 and str(M) == str(M)[::-1]:
            return M
    return 0


cnt = 0
for N in range(5_400_000 + 1, 10 ** 20):
    if f(N):
        print(N, f(N))
        cnt += 1
    if cnt == 5:
        break
