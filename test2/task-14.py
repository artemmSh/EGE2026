def converter(x, base):
    res = ''
    while x:
        res += str(x % base)
        x //= base
    return res[::-1]


ans = []
for x in range(10, 70001):
    num = 5 ** 2025 + 5 ** 400 - x
    num = converter(num, 5)
    ans.append([num.count('4'), x])

ans.sort(key=lambda x: (-x[0], -x[1]))
print(ans[0][1])
