def converter(x, base):
    res = ''
    while x:
        res += str(x % base)
        x //= base
    return res[::-1]


for x in range(1000, 0, -1):
    for y in range(1000, 0, -1):
        num = 5 ** 50 + 5 ** 30 - 5 ** x - y - 5 ** y - x
        if num > 0 and converter(num, 5).count('0') == 10:
            print(x * y)
            exit()
