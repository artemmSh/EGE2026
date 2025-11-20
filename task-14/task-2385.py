N = 16 ** 280 - 2 ** 761 + 14

count = 0

while N:
    if N % 4 == 0:
        count += 1
    N //= 4

print(count)
