def f(x, y, m):
    if x + y >= 77: return m % 2 == 0
    if m == 0: return 0
    h = [f(x + 3, y, m - 1),
         f(x, y + 3, m - 1),
         f(x * 3, y, m - 1),
         f(x, y * 3, m - 1)]
    return any(h) if m % 2 else all(h)


print('19)', sorted(s for s in range(1, 65) if f(12, s, 2))[0])
print('20)', *sorted(s for s in range(1, 65) if not f(12, s, 1) and f(12, s, 3))[:2])
print('21)', len([s for s in range(1, 65) if f(12, s, 4) and not f(12, s, 2)]))
