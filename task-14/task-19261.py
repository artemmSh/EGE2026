def converter(x, base):
    x = x[::-1]
    return sum(int(x[i], 36) * base ** i for i in range(len(x)))


from string import printable as alph

for x in alph[36::-1]:
    num = converter(f'98{x}31', 37) + converter(f'1{x}924', 37)
    if num % 21 == 0:
        print(num // 21)
        break
