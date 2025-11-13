def converter(x):
    res = ''
    while x:
        res += str(x % 4)
        x //= 4
    return res[::-1]


ans = []
for N in range(1, 1000000):
    R = converter(N)
    if R[0] == '3':
        R = R.replace('3', '1')
        R = '21' + R
    else:
        R = '1' + R[1:] + '12'
    R = int(R, 4)
    if R < 598:
        ans.append(N)
print(max(ans))
