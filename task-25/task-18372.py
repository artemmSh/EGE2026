def f(x):
    res = {1}
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            res |= {i, x // i}
    return sum(res) // len(res)


cnt = 0
for N in range(769999, 0, -1):
    if f(N) and f(N) % 100 == 12:
        cnt += 1
        print(N, f(N))
    if cnt == 5:
        break
