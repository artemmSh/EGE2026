for x in range(1, 3001):
    num = 9**150 + 9**30 - x
    cnt = 0
    while num:
        if num % 9 == 0:
            cnt += 1
        num //= 9
    if cnt == 122:
        print(x)
        break