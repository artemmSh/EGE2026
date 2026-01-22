def f(x, y):
    return (78125 != y + 4 * x) or (A > x) and (A > y)


for A in range(80000):
    if all(f(x, y) for x in range(1, 80000) for y in range(1, 80000)):
        print(A)
        break
