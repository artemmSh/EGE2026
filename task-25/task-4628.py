from fnmatch import fnmatch

for N in range(124065, 10 ** 8):
    if fnmatch(str(N), '12*4?65') and N % 161 == 0:
        print(N, N // 161)
