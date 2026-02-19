def f(x, y, cnt):
    if x == y and len(cnt) > 50: return 1
    if x > y: return 0
    return f(x + 2, y, cnt | {x + 2}) + f(3 * x, y, cnt | {3 * x}) + f(4 * x, y, cnt | {4 * x})


print(f(2, 400, set()))
