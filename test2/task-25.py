def dividers(x):
    res = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            if len(str(i)) > 1 and str(i)[-1] == '9':
                res.add(i)
            if len(str(x // i)) > 1 and str(x // i)[-1] == '9':
                res.add(x // i)
    return sorted(res)


cnt = 0
for i in range(800_001, 10_000_000):
    if dividers(i):
        cnt += 1
        print(i, min(dividers(i)))
    if cnt == 5:
        break
