def f(x):
    return (x % A == 0) or (x % 133 == 0) <= (x % 95 != 0)


for A in range(5000, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break
