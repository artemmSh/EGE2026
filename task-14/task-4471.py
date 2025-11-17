def converter(x, base):
    res = ''
    while x:
        res += str(x % base)
        x //= base
    return res[::-1]


num = 7*729**543 - 6*81**765 - 5*9**987 - 20

print(converter(num, 9).count('8'))

count = 0
while num:
    if num % 9 == 8:
        count += 1
    num//=9
print(count)