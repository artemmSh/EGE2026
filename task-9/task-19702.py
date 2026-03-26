from itertools import combinations

with open('files/task-19702.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    line = sorted(line, reverse=True)
    for c in combinations(line, 4):
        if len(set(c)) == 4:
            c = sorted(c)
            if c[1] - c[0] == c[2] - c[1] == c[3] - c[2]:
                cnt += 1
                break
print(cnt)
