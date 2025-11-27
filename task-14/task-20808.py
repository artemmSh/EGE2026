ans = []
for x in range(1, 2031):
    num = 7 ** 170 + 7 ** 100 - x
    cnt = 0
    while num:
        if num % 7 == 0:
            cnt += 1
        ans.append([cnt, x])
        num //= 7
ans.sort(key=lambda x: (x[0], x[1]))
print(ans[-1][-1])
