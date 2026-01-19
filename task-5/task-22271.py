ans = []
for N in range(1, 100_000):
    R = oct(N)[2:]
    if R[0] == '5':
        R = '11' + R.replace('1', '2')
    else:
        R = '2' + R[1:] + '10'
    R = int(R, 8)
    if R < 1354:
        ans.append([R, N])
ans.sort(key=lambda x: (-x[0], -x[1]))
print(ans[0][1])
