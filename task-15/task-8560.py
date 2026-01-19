for A in range(1, 100):
    if all(
            (2 * x + y != 136) or (z * y < 200) or (A ** 2 >= x + y) for x in range(1, 200) for y in range(1, 200) for
            z
            in range(1, 200)):
        print(A)
        break
