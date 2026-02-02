def div(x):
    res = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            res |= {i, x // i}
    if len(res) > 1:
        M = min(res) + max(res)
    else:
        M = 0
    return M


cnt = 0
for N in range(800_000 + 1, 10 ** 20):
    if div(N) and div(N) % 10 == 4:
        print(N, div(N))
        cnt += 1
    if cnt == 5:
        break
