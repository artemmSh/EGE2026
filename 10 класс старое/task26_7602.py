with open('26_7602.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file]

times.sort()
cells = [0] * K
counter = 0
last_cell = 0
for time in times:
    for i in range(K):
        if time[0] >= cells[i]:
            cells[i] = time[1] + 1
            counter += 1
            last_cell = i + 1
            break
print(counter, last_cell)



