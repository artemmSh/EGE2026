def f(x, y):
    if y == 15: return {x}
    return f(x + 10, y + 1) | f(x - 5, y + 1)


print(len(f(1, 0)))
