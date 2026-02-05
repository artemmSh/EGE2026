def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def fact(x):
    res = []
    while x % 2 == 0:
        res.append(x)
    i = 3
    while i < int(x ** 0.5) + 1:
        while x % i == 0:
            res.append(i)
            x //= i
        if len(res) > 2:
            return []
        i += 2
    if x > 2:
        res += [x]
    return res


cnt = 0
for N in range(5_000_000 + 1, 10 ** 20, 2):
    divs = fact(N)
    if len(divs) == 2 and divs[0] != divs[1]:
        if is_prime(abs(divs[0] - divs[1])):
            cnt += 1
            print(N, max(divs))
        if cnt == 5:
            break
