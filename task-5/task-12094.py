for N in range(1, 1_000_000):
    R = bin(N)[2:]
    if N % 8 == 0:
        R += R[-2:]
    else:
        R += bin(2 * (N % 8))[2:]
    R = int(R, 2)
    if R > 3000:
        print(N)
        break
