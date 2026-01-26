def converter(num, base):
    res = ''
    while num:
        res += str(num % base)
        num //= base
    return res[::-1] if res else '0'


ans = 10 ** 10
for N in range(100_000):
    R = converter(N, 4)
    if N % 2 == 0:
        R = '12' + R + converter(3 * (int(R[-1])), 4)
    else:
        R = '13' + R + '21'
    R = int(R, 4)
    if R > 50:
        ans = min(ans, R)
print(ans)
