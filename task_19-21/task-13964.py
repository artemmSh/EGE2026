def f(x, y, m):
    if x + y <= 108: return m % 2 == 0
    if m == 0: return 0
    h = [f(x - 2, y, m - 1), f(x, y - 2, m - 1), f(x // 2 + (x % 2), y, m - 1), f(x, y // 2 + (y % 2), m - 1)]
    return any(h) if m % 2 else all(h)


# print('19)', [s for s in range(49, 1000) if f(60, s, 2)]) -> 192
print('20)', [s for s in range(49, 1000) if not f(60, s, 1) and f(60, s, 3)])
print('21)', [s for s in range(49, 1000) if not f(60, s, 2) and f(60, s, 4)])
