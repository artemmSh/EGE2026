def f(x):
    return ((x % 263 == 0) and (x % A)) and x % 71 == 0


for A in range(20_000, 0, -1):
    if all(not f(x) for x in range(1, 20_000)):
        print(A)
        break
