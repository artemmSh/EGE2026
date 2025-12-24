def converter(x, base):
    res = ''
    while x:
        res += str(x % base)
        x //= base
    return res[::-1]


for x in range(1, 2301)[::-1]:
    num = 7 ** 350 + 7 ** 150 - x
    if converter(num, 7).count('0') == 200:
        print(x)
        break
