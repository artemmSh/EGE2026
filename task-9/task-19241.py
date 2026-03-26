with open('files/task-19241.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for line in data[::-1]:
    amount = sorted(line.count(i) for i in set(line))
    pov = [i for i in line if line.count(i) > 1]
    ne_pov = [i for i in line if i not in pov]
    if (amount == [1, 3, 3]) and ((sum(pov) / len(pov)) < ne_pov[0]):
        print(data.index(line) + 1)
        break
