from string import printable as alph

for x in alph[:27]:
    N = int(f'8{x}38{x}68', 27) + int(f'37{x}3163', 27)
    if N % 26 == 0:
        print(N // 26)
