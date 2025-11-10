for N in range(1, 1000000):
    R = bin(N)[2:]
    if N % 5 == 0:
        R += R[-3:]
    else:
        R += bin(5 * (N % 5))[2:]
    R = int(R, 2)
    if R > 256:
        print(N)
        break
