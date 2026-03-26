with open('files/task-14251.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for line in data:
    amount = sorted(line.count(i) for i in set(line))
    pov = [i for i in line if line.count(i) > 1]
    ne_pov = [i for i in line if i not in pov]
    if (amount == [1, 1, 1, 2, 2]) and (sum(pov) <= sum(i for i in line if i % 2)):
        print(sum(line))
        break
