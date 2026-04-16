def fact(x):
    res = []
    while x % 2 == 0:
        res.append(2)
        x //= 2
    i = 3
    while i * i < x + 1:
        while x % i == 0:
            res.append(i)
            x //= i
        if len(res) >= 3:
            break
        i += 2
    if x > 2:
        res.append(x)
    if len(res) == 3 and all('3' in str(i) or '4' in str(i) for i in res):
        return max(res)
    return 0


cnt = 0
for n in range(6_300_000 + 1, 10 ** 20):
    if fact(n):
        cnt += 1
        print(n, fact(n))
    if cnt == 5:
        break
