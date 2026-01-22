def f(x):
    return (A + 2 * x > 400 - A) and (A % 100 + 120 % A > 140)


for A in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break
