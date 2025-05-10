with open('26_9077.txt') as file:
    M, N = map(int, file.readline().split())
    scooters = dict()
    data = list()
    for i in range(1, M + 1):
        scooters[i] = []
    for i in file:
        data.append(list(map(int, i.split())))

data.sort()
counter_scooters = 0

for i in data:
    if len(scooters[i[2]]) == 0:
        scooters[i[3]].append(i[0] + i[1])
        counter_scooters += 1
    elif min(scooters[i[2]]) < i[0]:
        scooters[i[2]].remove(min(scooters[i[2]]))
        scooters[i[3]].append(i[0] + i[1])
    elif i[0] < min(scooters[i[2]]):
        counter_scooters += 1
        scooters[i[3]].append(i[0] + i[1])
print(counter_scooters)