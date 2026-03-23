with open('files/task-9778.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, line in enumerate(data, start=1):
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 1, 1, 1, 2]:
        pov = [i for i in line if line.count(i) > 1]
        ne_pov = [i for i in line if i not in pov]
        if pov[0] >= sum(ne_pov) / len(ne_pov):
            print(pos)
            break
