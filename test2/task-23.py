def f(x, y):
    if x == y:
        return 1
    if x < y or x == 13:
        return 0
    if x > y:
        return f(x - 1, y) + f(x - 2, y) + f(x // 3, y)


print(f(19, 6) * f(6, 4))
