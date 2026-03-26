with open('files/task-1962.txt') as file:
    data = [list(map(int, i.split())) for i in file]
cnt = 0

for line in data:
    line = sorted(line)
    if line[0] + line[1] > line[2]:
        cnt += 1
print(cnt)
