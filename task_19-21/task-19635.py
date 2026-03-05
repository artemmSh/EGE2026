def f(x, y, m):
    if x + y <= 100: return m % 2 == 0
    if m == 0: return 0
    h = [f(x - 3, y - 3, m - 1),
         f(x // 2, y, m - 1),
         f(x, y // 2, m - 1)]
    return any(h) if m % 2 else all(h)


# print('19)', sorted(s for s in range(53, 1000) if f(48, s, 2))[0]) -> 59
print('19)', [s for s in range(53, 1000) if not f(48, s, 1) and f(48, s, 3)])
print('19)', sorted(s for s in range(53, 1000) if not f(48, s, 2) and f(48, s, 4))[0])
