import math

with open('files/task-24347.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    s1 = line.count(max(line)) == 1
    s2 = all(line[i] not in (max(line), min(line)) for i in (0, -1))
    s3 = math.prod(sorted(line)[-3:]) % min(line) == 0
    if s1 + s2 + s3 == 1:
        cnt += 1
print(cnt)
