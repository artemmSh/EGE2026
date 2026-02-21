def f(x, y, cnt):
    if x % 2 == 0: cnt += 1
    if x == y: return 1
    if x > y or cnt > 15: return 0
    return f(x + 2, y, cnt) + f(x + 3, y, cnt) + f(2 * x + 1, y, cnt)


print(f(1, 55, 0))
