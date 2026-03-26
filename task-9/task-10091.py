from itertools import count

with open('files/task-10091.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    amount = sorted(line.count(i) for i in set(line))
    pov = [i for i in line if line.count(i) > 1]
    ne_pov = [i for i in line if i not in pov]
    if (amount == [1, 1, 1, 2, 2]) and ((sum(pov) / len(pov)) < (sum(line) / len(line))):
        cnt += 1
print(cnt)
