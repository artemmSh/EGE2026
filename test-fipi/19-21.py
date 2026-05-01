def f(x, y, m):
    if x + y >= 154: return m % 2 == 0
    if m == 0: return 0
    h = [f(x + 4, y, m - 1),
         f(x, y + 4, m - 1),
         f(x * 3, y, m - 1),
         f(x, y * 3, m - 1)]
    return any(h) if m % 2 else all(h)

# print('19)', [s for s in range(1, 143) if f(11, s, 2)]) -> 16
# print('20)', [s for s in range(1, 143) if not f(11, s, 1) and f(11, s, 3)]) -> 39 40
# print('21)', [s for s in range(1, 143) if not f(11, s, 2) and f(11, s, 4)]) -> 41
