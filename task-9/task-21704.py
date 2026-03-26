with open('files/task-21704.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for line in data:
    if (sorted(line, reverse=True) == line) and (min(line) + max(line)) / 2 > (sum(line) - (min(line) + max(line))) / 5:
        print(sum(line))
        break
