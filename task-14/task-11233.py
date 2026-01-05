from string import printable as alph

for x in alph[:26]:
    num = int(f'27{x}98876', 26) + int(f'26{x}51', 26) + int(f'15{x}47', 26) + int(f'62{x}5', 26)
    if num % 25 == 0:
        print(num // 25)
