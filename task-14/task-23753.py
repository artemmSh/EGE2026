from string import printable as alph

for x in alph[28::-1]:
    num = int(f'923{x}874', 29) + int(f'524{x}6152', 29)
    if num % 28 == 0:
        print(num // 28)
        break