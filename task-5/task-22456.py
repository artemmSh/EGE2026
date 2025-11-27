for N in range(1, 100_000):
    R = bin(N)[2:]
    if not sum(map(int, R)) % 2:
        R = '11' + R[2:] + '1'
    elif R.count('0') < R.count('1'):
        R += '0'
    else:
        R += '1'
    R = int(R, 2)
    if R > 271:
        print(N)
        break
