def cif(x, y):
    return x % 10 == y % 10


def f(x):
    return ((x % 10 != 5) and cif(x, 4)) <= (x > A - 11)


for A in range(1000, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break
