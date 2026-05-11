from fnmatch import fnmatch

for n in range(9874, 10 ** 10 + 1, 9874):
    if fnmatch(str(n), '89*6?7?9?'):
        print(n, n // 9874)
