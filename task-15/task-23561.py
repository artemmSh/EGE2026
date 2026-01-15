def div(n, m):
    if n % m == 0:
        return True
    return False


def f(A):
    for x in range(1000):
        f = div(x, 128) <= ((not div(x, A)) <= (not div(x, 80)))
        if not f:
            return False
    return True


for A in range(10000, 0, -1):
    if f(A):
        print(A)
        break
