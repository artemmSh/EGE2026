from string import printable as alph

for x in alph[:19]:
    N = int(f'98{x}79641', 19) + int(f'36{x}14', 19) + int(f'73{x}4', 19)
    if N % 18 == 0:
        print(x, N // 18)
