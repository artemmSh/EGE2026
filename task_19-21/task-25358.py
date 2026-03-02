def f(x, m):
    if x >= 125: return m % 2 == 0
    if m == 0: return 0
    h = [f(x + 2, m - 1), f(x + 4, m - 1), f(x * 2, m - 1)]
    return any(h) if m % 2 else all(h)


print('19)', [s for s in range(1, 125) if f(s, 2)])
print('20)', [s for s in range(1, 125) if not f(s, 1) and f(s, 3)])
print('21)', [s for s in range(1, 125) if not f(s, 2) and f(s, 4)])
