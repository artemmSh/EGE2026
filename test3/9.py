with open('files/9.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, line in list(enumerate(data, start=1)):
    amount = sorted(line.count(i) for i in set(line))
    pov = [i for i in line if line.count(i) > 1]
    ne_pov = [i for i in line if i not in pov]
    if (amount == [1, 1, 1, 1, 2]) and (pov[0] >= (sum(ne_pov) / len(ne_pov))):
        print(pos)
        break
