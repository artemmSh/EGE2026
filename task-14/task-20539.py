def converter(x, base):
    res = ''
    while x:
        res += str(x % base)
        x //= base
    return res[::-1]

for a in range(1, 100_000):
    num = 3**10 + 3**7 + 3**3 + 2 - a
    if converter(num, 3).count('0') == converter(num, 3).count('1') == converter(num, 3).count('2'):
        print(a)
        break
