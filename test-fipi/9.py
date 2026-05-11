with open('files/9.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    s1 = max(line) < (sum(line) - max(line))
    s2 = sorted(line)[0] + sorted(line)[3] != sorted(line)[1] + sorted(line)[2]
    if s1 and s2:
        cnt += 1
print(cnt)
