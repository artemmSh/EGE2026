res = set()


def f(x, y):
    if y == 8:
        if x in range(1000, 1025):
            res.add(x)
    else:
        f(x + 1, y + 1)
        f(x + 5, y + 1)
        f(3 * x, y + 1)


f(1, 0)
print(len(res))
