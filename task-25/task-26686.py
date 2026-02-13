def fact(x):
    res = []
    while x % 2 == 0:
        res.append(2)
        x //= 2

    i = 3
    while i < int(x ** 0.5) + 1:
        while x % i == 0:
            res.append(i)
            x //= i
        i += 2
    if x > 2:
        res.append(x)

    return res


cnt = 0
for N in range(89_428_304 + 1, 10 ** 20):
    divs = fact(N)
    if len(divs) >= 6 and N % sum(divs) == 0:
        cnt += 1
        print(N, sum(divs))
    if cnt == 6:
        break
