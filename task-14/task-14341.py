from string import printable as alph

for x in alph[:22]:
    num = int(f'56{x}c20', 22) + int(f'89f{x}2', 22) + int(f'h24{x}k21', 22)
    if num % 21 == 0:
        print(num // 21)
        break
