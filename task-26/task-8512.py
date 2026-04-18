with open('files/26_8512.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]

data.sort()

cells = [0] * K
cnt = 0
last_cell = 0
for pas in data:
    for i in range(K):
        if pas[0] > cells[i]:
            cells[i] = pas[1]
            cnt += 1
            last_cell = i + 1
            break
print(cnt, last_cell)
