from string import printable as alph


def converter(x, base):
    res = ''
    while x:
        res += alph[x % base]
        x //= base
    return res[::-1]


ans = []
for N in range(11, 100000):
    R = converter(N, 3)
    cnt_even = sum([1 for i in range(len(R)) if int(R[i], 36) % 2 == 0])
    cnt_odd = sum([1 for i in range(len(R)) if int(R[i], 36) % 2 != 0])
    if cnt_even > cnt_odd:
        R = '22' + R
    else:
        R = '11' + R
    R = int(R, 3)
    if R > 100:
        ans.append(R)
print(min(ans))
