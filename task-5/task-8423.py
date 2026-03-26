for N in range(1, 10 ** 6)[::-1]:
    R = bin(N)[2:]
    if N % 5 == 0:
        R += bin(5)[2:]
    else:
        R += '1'
    if int(R, 2) % 7 == 0:
        R += bin(7)[2:]
    else:
        R += '1'
    R = int(R, 2)
    if R < 1_855_663:
        print(N)
        break
