from fnmatch import fnmatch

for N in range(1917, 10 ** 10, 1917):
    if fnmatch(str(N), '3?12?14*5'):
        print(N, N // 1917)
