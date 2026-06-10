def f(x, y):
    return (x < A) and (y < 3 * A) or (2 * x + y > 128)


for A in range(1, 100 ** 100):
    if all(f(x, y) for x in range(1, 5000) for y in range(1, 5000)):
        print(A)
        break
