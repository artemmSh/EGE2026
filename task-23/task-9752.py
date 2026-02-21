def f(x, y):
    if x == y: return 1
    if x > y or x == 17: return 0
    return f(x + 2, y) + f(x + 3, y) + f(2 * x, y)


print(f(3, 10) * f(10, 25))
