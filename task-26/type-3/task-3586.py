with open('../files/26_3586.txt') as file:
    N = int(file.readline())
    rows = dict()
    for i in file:
        row, pos = map(int, i.split())
        if row not in rows:
            rows[row] = [pos]
        else:
            rows[row].append(pos)
            rows[row].sort()

rows_copy = rows.copy()
rows = sorted(rows, reverse=True)
sorted_rows = dict()
for row in rows:
    sorted_rows[row] = rows_copy[row]
ans = []
for row in sorted_rows:
    positions = sorted_rows[row]
    for i in range(len(positions) - 1):
        ans.append([positions[i + 1] - positions[i] - 1, row])

ans.sort(reverse=True)
print(*ans[0][::-1])
