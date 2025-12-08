for p in range(30, 37):
    for s in range(10, 35):
        num = int('r4', p - 1) + int('b0', s + 2) + int('t3nk4', p)
        if num == 23593399:
            print(p * s)
