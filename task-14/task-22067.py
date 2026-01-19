from string import printable as alph

num = 3 * 17 ** 777 + 15 * 17 ** 250 - 6 * 17 ** 100 + 2


def converter(x, base):
    res = ''
    while x:
        res += alph[x % base]
        x //= base
    return res[::-1]


print(sum(1 for i in set(converter(num, 17)) if int(i, 17) % 2 == 0))
