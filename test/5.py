for N in range(1, 1000000):
    binary = bin(N)[2:]
    if N % 3 == 0:
        binary += '111'
    else:
        binary += bin(3*(N%3))[2:]
    R = int(binary, 2)
    if R < 130:
        print(N)