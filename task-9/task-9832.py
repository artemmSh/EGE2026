with open('files/task-9832.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for line in data:
    s1 = [line.count(i) for i in line]
    if s1.count(2) == 4 and s1.count(1) == 3 and line.count(max(line)) == 1:
        print(sum(line))
        break
