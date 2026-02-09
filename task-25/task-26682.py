from math import prod


def div(x):
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res |= {i, x // i}
    return res


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
            if len(res) > 9:
                break
        i += 2
    if x > 2:
        res.append(x)
    return res


cnt = 0
for N in range(5_200_000 + 1, 10 ** 20):
    if len(fact(N)) == 9 and prod(fact(N)) == N and len(div(N)) % 90 == 0:
        cnt += 1
        print(N, max(fact(N)))
    if cnt == 5:
        break
