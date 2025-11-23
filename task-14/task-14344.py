for p in range(16, 37):
    N = int(f'17496', p) + int(f'91f83', p) + int(f'd9543', p)
    if N % 12 == 0:
        print(N // 12)
        break
