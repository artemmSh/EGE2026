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
            if len(res) > 4:
                break
        i += 2
    if x > 2:
        res.append(x)
    return res


cnt = 0
for N in range(7_305_678 + 1, 10 ** 20):
    if len(f(N)) == 4 and str(sum(f(N))) == str(sum(f(N)))[::-1]:
        cnt += 1
        print(N, sum(f(N)))
    if cnt == 5:
        break
