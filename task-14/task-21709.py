def converter(x, base):
    res = ''
    while x:
        res += str(x % base)
        x //= base
    return res[::-1]
ans = []
for x in range(1, 3001):
    num = 4**210 + 4**110 - x
    ans.append([converter(x, 4).count('0'), x])

print(sorted(ans, key=lambda x: (-x[0], x[1]))[0][1])


