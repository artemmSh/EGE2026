def f(x):
    res = []
    while x % 2 == 0:
        x //= 2
    i = 3
    while i * i < x + 1:
        if x % i == 0:
            x //= i
            if i % 10 == 7:
                res.append(i)
        i += 2
    if x > 2 and x % 10 == 7:
        res.append(x)
    if len(res) > 1:
        return sum(res) // len(res)
    return 0


cnt = 0
for N in range(750_000 - 1, 0, -1):
    if f(N) and f(N) % 111 == 0:
        cnt += 1
        print(N, f(N))
    if cnt == 5:
        break
