with open('files/task-20899.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    s1 = max(line) < (sum(line) - max(line))
    s2 = len(set(line)) == 3
    if s1 and s2:
        cnt += 1
print(cnt)
