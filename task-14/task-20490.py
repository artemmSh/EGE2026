def converter(x, base):
    res = ''
    while x:
        res += str(x % base)
        x //= base
    return res[::-1]


for x in range(2005, 0, -1):
    num = 4 ** 163 * 5 + 12 ** 62 - x
    num = converter(num, 5)
    if num.count('1') < num.count('4'):
        print(x)
        break
