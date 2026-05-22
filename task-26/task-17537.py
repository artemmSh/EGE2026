with open('files/26_17537.txt') as file:
    N, M, K = map(int, file.readline().split())
    rows = [M] * K
    for i in file:
        row, seat = map(int, i.split())
        if row < rows[seat - 1]:
            rows[seat - 1] = row - 1

ans_1 = max(min(rows[i], rows[i + 1]) for i in range(len(rows) - 1))
ans_2 = len(rows) - rows[::-1].index(ans_1) + 1
print(ans_1, ans_2)
