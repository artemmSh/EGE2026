for x in range(1, 100_000):
    cnt = 0
    num = 7 ** 666 + 7 ** 333 + 49 ** x - 343
    while num:
        if num % 7 == 6:
            cnt += 1
        num //= 7
    if cnt == 49:
        print(x)
        break
