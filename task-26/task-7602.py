with open('files/26_7602.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    passengers = [list(map(int, i.split())) for i in file]

passengers.sort()

cells = [0] * K
cnt = 0
last_cell = 0
for pas in passengers:
    for i in range(K):
        if pas[0] > cells[i]:
            cells[i] = pas[1]
            cnt += 1
            last_cell = i + 1
            break
print(cnt, last_cell)
