def f(x, y, m):
    if x + y >= 211: return m % 2 == 0
    if m == 0: return 0
    h = [f(x + 1, y, m - 1), f(x, y + 1, m - 1), f(x * 2, y, m - 1), f(x, y * 2, m - 1)]
    return any(h) if m % 2 else all(h)


print('19)', [s for s in range(1, 194) if f(17, s, 2)])  # 49
print('20)', [s for s in range(1, 194) if not f(17, s, 1) and f(17, s, 3)])  # 88, 96
print('21)', [s for s in range(1, 194) if not f(17, s, 2) and f(17, s, 4)])  # 87
