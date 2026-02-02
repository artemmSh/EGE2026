for N in range(100_000, 0, -1):
    R = bin(2 + N)[2:]
    for i in range(2):
        R += str(sum(map(int, R)) % 2)
    R = int(R, 2)
    if R < 61:
        print(N)
        break
