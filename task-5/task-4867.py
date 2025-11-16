for N in range(2, 1000_000):
    summ = 0
    N = str(N)
    a = sum(map(int, N[1::2]))
    b = sum([i for i in range(len(N)) if int(i) % 2 == 0])
    res = abs(a - b)
    if res == 9:
        print(N)
        break
