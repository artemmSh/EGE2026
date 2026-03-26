with open('files/task-23747.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for line in data[::-1]:
    amount = sorted(line.count(i) for i in set(line))
    pov = [i for i in line if line.count(i) > 1]
    ne_pov = [i for i in line if i not in pov]
    c1 = (amount == [1, 1, 1, 1, 3])
    c2 = pov and ((sum(ne_pov) / len(ne_pov)) <= pov[0])
    if c1 and c2:
        print(sum(line))
        break
