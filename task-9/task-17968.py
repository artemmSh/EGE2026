with open('files/task-17968.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    s1 = max(line) < (sum(line) - max(line))
    s2 = sum(i for i in line if i % 2 == 0) == sum(i for i in line if i % 2)
    if s1 and s2:
        cnt += 1
print(cnt)
