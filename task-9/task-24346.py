with open('files/task-24346.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, line in list(enumerate(data, start=1))[::-1]:
    pov = [i for i in line if line.count(i) > 1]
    ne_pov = [i for i in line if i not in pov]
    s1 = pov and ne_pov
    s2 = sum(pov) ** 2 > sum(ne_pov) ** 2
    s3 = sum(line) % 2
    if s1 and s2 and s3:
        print(pos)
        break
