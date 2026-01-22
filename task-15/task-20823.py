for A in range(1, 1000):
    if all((x & A == 0) <= ((x & 77 == 0) and (x & 44 == 0)) for x in range(1, 1000)):
        print(A)
        break
