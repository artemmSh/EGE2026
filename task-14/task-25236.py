for p in range(36, 10, -1):
    for x in range(1, 500_000):
        num1 = int('1', 36) * p ** 0 + int('a', 36) * p ** 1 + int('9', 36) * p ** 2 + int('2', 36) * p ** 3
        num2 = int('1', 36) * p ** 0 + int('7', 36) * p ** 1 + int('7', 36) * p ** 2 + int('7', 36) * p ** 3 + int('4', 36) * p ** 4
        num3 = int('a', 36) * p ** 0 + int('2', 36) * p ** 1 + int('1', 36) * p ** 2
        num4 = 1000000
        num5 = x
        if num1 + num2 + num3 == num4 + num5:
            print(p)
            break