def f(x):
    res = []
    while x % 2 == 0:
        res.append(2)
        x //= 2
    i = 3
    while i <= int(x ** 0.5) + 1:
        while x % i == 0:
            res.append(i)
            x //= i
        i += 2
        if len(res) > 5:
            break
    if x > 2:
        res.append(x)
    return sorted(res)


cnt = 0
for N in range(13_475_124 + 1, 10 ** 20):
    if len(f(N)) == 5 and all(str(i).count('5') > 0 for i in f(N)):
        cnt += 1
        print(N, f(N)[-1])
    if cnt == 5:
        break
