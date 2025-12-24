from string import printable as alph

for x in alph[21::-1]:
    num = int(f'a23{x}ac0', 22) + int(f'gb{x}21670', 22)
    if num % 21 == 0:
        print(num // 22)
        break