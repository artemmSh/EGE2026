from string import printable as alph

for x in alph[:16]:
    N = int(f'11{x}73', 16) + int(f'94662{x}53{x}', 16) + int(f'6{x}41', 16) + int(f'31{x}77', 16) + int(f'9{x}82{x}{x}181', 16)
    if N % 15 == 0:
        print(N // 15)
        break