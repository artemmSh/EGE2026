from string import printable as alph

for x in alph[1:13]:
    N = int(f'9{x}ab', 13) + int(f'{x}46c', 16) - int(f'b7{x}', 15)
    if N % 14 == 0:
        print(N // 14)
        break
