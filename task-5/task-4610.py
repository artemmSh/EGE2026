ans = []
for N in range(1, 10000000):
    R = bin(N)[2:]
    if R.count('1') % 2 == 0:
        R = '10' + R[2:] + '0'
    else:
        R = '11' + R[2:] + '1'
    R = int(R, 2)
    if R < 35:
        ans.append(N)
print(ans[-1])
