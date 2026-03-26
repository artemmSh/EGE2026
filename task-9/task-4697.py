with open('files/task-4697.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    amount = sorted(line.count(i) for i in set(line))
    pov = [i for i in line if line.count(i) > 1]
    ne_pov = [i for i in line if i not in pov]
    # s1 = (amount == [1, 1, 1, 1, 2])
    # s2 = ((sum(ne_pov) / len(ne_pov)) <= sum(pov))
    if (amount == [1, 1, 1, 1, 2]) and ((sum(ne_pov) / len(ne_pov)) <= sum(pov)):
        cnt += 1
print(cnt)
