from string import printable as alph

for x in alph[:23]:
    N = int(f'7{x}38596', 23) + int(f'14{x}36', 23) + int(f'61{x}7', 23)
    if N % 22 == 0:
        print(x, N // 22)
