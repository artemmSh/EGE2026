for N in range(1, 100_000):
    R = bin(N)[2:]
    if not  N % 2:
        R += bin(R.count('1'))[2:]
    else:
        R = '1' + R + '101'
    R = int(R, 2)
    if R > 350:
        print(N)
        break