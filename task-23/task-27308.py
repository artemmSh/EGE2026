def f(x, y):
    if x == y: return 1
    if x < y: return 0
    return f(x - 3, y) + f(x - 5, y) + f(x // 3, y)


a_and_b = f(80, 38) * f(38, 18) * f(18, 3)
only_a = f(80, 38) * f(38, 3) - f(80, 38) * f(38, 18) * f(18, 3)
only_b = f(80, 18) * f(18, 3) - f(80, 38) * f(38, 18) * f(18, 3)
print(a_and_b + only_a + only_b)
