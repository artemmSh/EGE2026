for x in range(1, 1_000_000):
    N = 3 * 7 ** (x + 1) + 13 * 7 ** (x + 2) + 31 * 7 ** (3 * x) + 1 * 7 ** (2 * x)
    total = 0
    while N:
        total += N % 7
        N //= 7
    if total == 18:
        print(x)
        break
