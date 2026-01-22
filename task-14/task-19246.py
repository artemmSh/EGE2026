from string import printable as alph

for x in alph[24::-1]:
    num = int(f'11353{x}12', 25) + int(f'135{x}21', 25)
    if not num % 24:
        print(num // 24)
        break
