from fnmatch import fnmatch


def div(x):
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res |= {i, x // i}
    return res


for N in range(53, 10 ** 7 + 1, 53):
    if fnmatch(str(N), '*2?2*') and str(N) == str(N)[::-1] and len(div(N)) > 30:
        print(N, sum(div(N)))
