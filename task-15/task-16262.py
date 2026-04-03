def f(x, y):
    return ((A < x) or (x ** 2 - 7 * x + 10 > 0)) and ((A >= y) or (y ** 2 + 7 * y + 12 > 0))


cnt = 0
for A in range(-1_00, 1_00):
    if all(f(x, y) for x in range(-1_00, 1_00) for y in range(-1_00, 1_00)):
        cnt += 1
print(cnt)
