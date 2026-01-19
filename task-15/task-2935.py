for A in range(5000, 0, -1):
    if all((2 * y + 3 * x != 135) or (y > A) or (x > A) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)
        break
