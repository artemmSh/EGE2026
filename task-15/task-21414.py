for A in range(1000):
    if all((5 < y) or (x > 32) or (x + 2 * y < A) for x in range(1000) for y in range(1000)):
        print(A)
        break
