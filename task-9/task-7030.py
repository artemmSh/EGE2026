with open('files/task-7030.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    if len(set(line)) == 3 and (sorted(set(line))[2] ** 2 == (sorted(set(line))[0] ** 2 + sorted(set(line))[1] ** 2)):
        cnt += 1
print(cnt)
