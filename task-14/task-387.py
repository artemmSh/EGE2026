N = 51 * 7 ** 12 - 7 ** 3 - 22

total = 0

while N:
    total += N % 7
    N //= 7
print(total)
