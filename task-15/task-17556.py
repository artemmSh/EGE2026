def div(n, m):
    if n % m == 0:
        return True
    return False


def f(A):
    for x in range(1000):
        B = 70 <= x <= 90
        f = div(x, A) or (B <= (not div(x, 22)))
        if not f:
            return False
    return True


for A in range(10000, 0, -1):
    if f(A):
        print(A)
        break
