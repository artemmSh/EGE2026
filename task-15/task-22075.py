def dig(x, y):
    return x // 10 ** (len(str(x)) - 1) == y // 10 ** (len(str(y)) - 1)


def f(x):
    return ((not dig(x, 28)) and dig(x, 47)) <= (x > A - 20)


for A in range(10 ** 5, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break
