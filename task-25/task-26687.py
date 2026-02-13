def divs(x):
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
        if len(res) > 8:
            return []
    if x > 2:
        res.append(i)
    return res


cnt = 0
for N in range(89_427_150 + 1, 10 ** 20):
    M = divs(N)
    if len(M) == 8 and M.count(min(M)) == 1 and len(set(M)) == 6:
        cnt += 1
        print(N, max(M))
    if cnt == 7:
        break
