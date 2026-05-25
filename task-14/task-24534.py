ans = []
for x in range(1, 11500 + 1):
    num = 7 ** 270 + 7 ** 170 + 7 ** 70 - x
    cnt = 0
    while num:
        if num % 7 == 0:
            cnt += 1
        num //= 7
    ans.append([cnt, x])
print(max(ans)[1])
