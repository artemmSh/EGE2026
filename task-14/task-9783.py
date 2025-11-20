from string import printable as alph

for x in alph[:22]:
    N = int(f'18{x}89957', 22) + int(f'80{x}33', 22) + int(f'521{x}6', 22)
    if N % 21 == 0:
        print(x, N // 21)
