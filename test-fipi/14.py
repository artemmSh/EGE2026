cnt = 0
num = 5 * 1296 ** 2021 - 4 * 216 ** 2022 + 3 * 36 ** 2023 - 2 * 6 ** 2024 - 2025
while num:
    if (num % 36) % 2 == 0:
        cnt += 1
    num //= 36
print(cnt)
