with open('26_20910.txt') as file:
    N, M, K = map(int, file.readline().split())
    rows = [M] * (K + 1)
    for i in file:
        row, seat = map(int, i.split())
        rows[seat] = min(rows[seat], row - 1)
ans = []
for i in range(K):
    previous, current = rows[i], rows[i + 1]
    ans.append([min(previous, current), i])
ans.sort(key=lambda x: (-x[0], x[1]))
print(ans[0])
