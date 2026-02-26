def f(x, y, m):
    if x + y >= 65: return m % 2 == 0
    if m == 0: return False
    h = [f(x + 1, y, m - 1), f(x, y + 1, m - 1), f(x * 3, y, m - 1), f(x, y * 3, m - 1)]
    return any(h) if m % 2 else all(h)


# print('19)', [s for s in range(1, 59) if f(s, 6, 2)])
print('19)', [s for s in range(1, 59) if f(s, 6, 3) and not f(s, 6, 1)])
print('19)', [s for s in range(1, 59) if f(s, 6, 4) and not f(s, 6, 2)])
