for x in range(1, 3001)[::-1]:
    num = 9*11**210 + 8*11**150 - x
    cnt = 0
    while num:
        if num % 11 == 0:
            cnt += 1
        num //= 11
    if cnt == 60:
        print(x)
        break