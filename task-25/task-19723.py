from fnmatch import *

for N in range(451, 10 ** 9, 451):
    if fnmatch(str(N), '10?451*3'):
        print(N, N // 451)
