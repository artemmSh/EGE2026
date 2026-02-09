def f(x):
    res = []
    while x % 2 == 0:
        res.append(2)
        x //= 2
    i = 3
    while i < int(x ** 0.5) + 1:
        while x % i == 0:
            res.append(i)
            x //= i
            if len(res) > 2:
                break
        i += 2
    if x > 2:
        res.append(x)
    return sorted(res)


cnt = 0
for N in range(6_086_055 + 1, 10 ** 20):
    if len(f(N)) == 2 and all(str(i).count('6') == 1 for i in f(N)):
        cnt += 1
        print(N, f(N)[-1])
    if cnt == 5:
        break
