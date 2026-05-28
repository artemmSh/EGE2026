with open('files/9.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, line in enumerate(data, start=1):
    count = sorted(line.count(i) for i in set(line))
    pov = [i for i in line if line.count(i) > 1]
    ne_pov = [i for i in line if i not in pov]
    s1 = count == [1, 1, 1, 2, 2]
    s2 = sum(pov) / len(ne_pov) < max(ne_pov)
    if s1 and s2:
        print(pos)
        break
