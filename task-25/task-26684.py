from math import prod


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
        i += 2
    if x > 2:
        res.append(x)
    return sorted(res)


cnt = 0
for N in range(5_000_000 + 1, 10 ** 20):
    if N % 100 == 12 and prod(fact(N)) == N and any(fact(N).count(i) == 5 for i in fact(N)):
        cnt += 1
        print(N, (fact(N)))
    if cnt == 5:
        break
