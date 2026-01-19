for A in range(5000):
    if all((x >= 27) or (2 * x < 3 * y) or ((x + 2) * (y - 3) < A) for x in range(1000) for y in range(1000)):
        print(A)
        break
