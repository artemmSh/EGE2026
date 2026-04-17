def f(x, m):
    if x >= 4:
        h = [f(x - 1, m - 1), f(x - 2, m - 1), f(x - 4, m - 1)]
    elif x >= 2:
        h = [f(x - 1, m - 1), f(x - 2, m - 1), f(x - 4, m - 1)]
    elif x >= 1:
        h = [f(x - 1, m - 1)]
    else:
        return m % 2 == 0
    if m == 0: return 0
    return any(h) if m % 2 else all(h)


# print('19)', [s for s in range(1, 16) if f(s, 2)]) -> 8
print('20)', [s for s in range(1, 16) if not f(s, 3) and f(s, 5)])
# print('21)', max(s for s in range(1, 16) for i in range(1, 100, 2) if not f(s, i))) -> 15
