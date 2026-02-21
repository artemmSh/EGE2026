def fact(x):
    res = set()
    while x % 2 == 0:
        res.add(2)
        x //= 2

    i = 3
    while i * i < x + 1:
        while x % i == 0:
            res.add(i)
            x //= i
        i += 2
    if x > 2:
        res.add(x)
    res = sorted(res)
    if len(res) >= 4:
        return res[0] + res[1] + res[-2] + res[-1]
    return 0


cnt = 0
for N in range(456_789 + 1, 10 ** 20):
    if fact(N) % 114 == 39:
        cnt += 1
        print(N, fact(N))
    if cnt == 5:
        break
