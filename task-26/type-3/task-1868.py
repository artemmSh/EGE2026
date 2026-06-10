with open('../files/26_1868.txt') as file:
    N = int(file.readline())
    rows = dict()
    for i in file:
        row, seat = map(int, i.split())
        if row not in rows:
            rows[row] = [seat]
        else:
            rows[row].append(seat)
            rows[row].sort()

rows_copy = rows.copy()
rows = sorted(rows, reverse=True)
sorted_rows = dict()
for row in rows:
    sorted_rows[row] = rows_copy[row]

for row in sorted_rows:
    seats = sorted_rows[row]
    for i in range(len(seats) - 1):
        if seats[i + 1] - seats[i] == 3:
            print(row, seats[i] + 1)
            exit()
