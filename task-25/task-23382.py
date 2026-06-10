def f(x):
    res = []
    while x % 2 == 0:
        x //= 2
        res.append(2)
    i = 3
    while i * i < x + 1:
        while x % i == 0:
            x //= i
            res.append(i)
        i += 2
        if len(res) >= 2:
            break
    if x > 2:
        res.append(x)
    if len(res) == 2 and all(str(i).count('2') == 1 for i in res):
        return max(res)
    return 0


cnt = 0
for n in range(6_651_221, 100 ** 100):
    if f(n):
        cnt += 1
        print(n, f(n))
    if cnt == 5:
        break
