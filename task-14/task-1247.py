N = 729 ** 8 - 3 ** 18 + 85

cnt = 0

while N:
    if N % 9 == 0:
        cnt += 1
    N //= 9
print(cnt)
