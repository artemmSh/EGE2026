from string import printable as alph

for x in alph[24::-1]:
    num = int(f'a4{x}7f2', 25) + int(f'n{x}g5{x}h', 25) + int(f'74{x}m26', 25)
    if num % 24 == 0:
        print(num // 24)
        break
