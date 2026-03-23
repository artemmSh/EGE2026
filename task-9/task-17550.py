with open('files/task-17550.txt') as file:
    data = [list(map(int, i.split())) for i in file]
cnt = 0
for line in data:
    amount = [line.count(i) for i in set(line)]
    pov = [i for i in line if line.count(i) > 1]
    ne_pov = [i for i in line if i not in pov]
    s1 = sorted(amount) == [1, 1, 1, 3]
    s2 = sum(pov) ** 2 > sum(ne_pov) ** 2
    if s1 and s2:
        cnt += 1
print(cnt)
