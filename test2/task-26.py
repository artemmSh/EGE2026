with open('26.txt') as file:
    N = int(file.readline())
    data = dict()
    for i in file:
        tmp = list(map(int, i.split()))
        if tmp[0] not in data:
            data[tmp[0]] = tmp[1:]
        else:
            data[tmp[0]].append(tmp[2])

sum_tmp = 0
for key in data:
    sum_tmp += data[key][0]
avg = sum_tmp / N

expensive = dict()
cheap = dict()
for key in data:
    if data[key][0] > avg:
        expensive[key] = data[key]
    else:
        cheap[key] = data[key]

expensive_sorted = sorted(expensive,
                          key=lambda x: (-expensive[x][1:].count(0), -expensive[x][0], expensive[x][1:].count(1)))
sales_leader_id = expensive_sorted[0]
print(expensive[sales_leader_id][0] * expensive[sales_leader_id][1:].count(0), expensive[sales_leader_id][1:].count(1))
