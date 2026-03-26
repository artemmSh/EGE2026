with open('files/task-17863.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    amount = sorted(line.count(i) for i in set(line))
    pov = [i for i in line if line.count(i) > 1]
    ne_pov = [i for i in line if i not in pov]
    if (amount == [1, 1, 1, 3]) and (sum(pov) ** 2 > sum(ne_pov) ** 2):
        cnt += 1
print(cnt)
