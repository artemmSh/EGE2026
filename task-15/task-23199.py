def f(A):
    for x in range(1000):
        for y in range(1000):
            f = (x * y > A) or (x > y) or (11 > x)
            if not f:
                return False
    return True


for A in range(5000, -1, -1):
    if f(A):
        print(A)
        break
