from string import printable as alph


def converter(x, base):
    res = ''
    while x:
        res += alph[x % base]
        x //= base
    return res[::-1]


for x in range(1, 27001):
    num = 3 * 27 ** 9 + 2 * 27 ** 6 + 27 ** 3 - x
    if converter(num, 27).count('0') == 6:
        print(x)
        break
