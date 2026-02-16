def max_div(x):
    res = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            res |= {i, x // i}
    return max(res)


cnt = 0
for N in range(10 ** 9 + 1, 10 ** 20):
    if str(N) == str(N)[::-1] and max_div(N) % 7 == 0:
        cnt += 1
        print(N, max_div(N))
    if cnt == 5:
        break
