def converter(x):
    res = ''
    while x:
        res += str(x % 8)
        x //= 8
    return res[::-1]


ans = []
for N in range(1, 1000000):
    R = converter(N)
    count = R.count('0') + R.count('2') + R.count('4') + R.count('6')
    if count % 2 != 0:
        R = R[-3:] + '46'
    else:
        R = converter(5 * (N % 8)) + R
    R = int(R, 8)
    if N >= 80:
        ans.append(R)
print(min(ans))
