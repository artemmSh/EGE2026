with open('26_9171.txt') as file:
    M, K, N = map(int, file.readline().split())
    stations = dict()
    for i in range(M):
        stations[i + 1] = []
    for x in file:
        start, end = map(int, x.split())
        stations[start].append(end)

for i in stations.values():
    i.sort(reverse=True)

seats = [0] * K
cnt_distillations = 0
cnt_lucky_passengers = 0

for i in stations:
    while i in seats:
        seats[seats.index(i)] = 0
    for passenger in stations[i]:
        if 0 in seats:
            seats[seats.index(0)] = passenger
            cnt_lucky_passengers += 1
        else:
            break
    if 0 not in seats:
        cnt_distillations += 1
print(cnt_lucky_passengers, cnt_distillations)
