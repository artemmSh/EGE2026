from string import printable as alph


def converter(x, base):
    res = ''
    while x:
        res += alph[x % base]
        x //= base
    return res[::-1]


ans = []
for N in range(151, 100_000):
    R = converter(N, 16).lower()
    R = R.replace('a', '1')
    cnt_even = sum([1 for i in R if int(i, 16) % 2 == 0])
    if cnt_even > 2:
        R += 'b'
    else:
        R = 'f' + R
    R = int(R, 16)
    if R > 3500:
        ans.append([R, N])
ans.sort(key=lambda x: (x[0], x[1]))
print(ans[0][-1])
