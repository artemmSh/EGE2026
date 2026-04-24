with open('files/26_17643.txt') as file:
    all_costs = list()
    data = dict()
    N = int(file.readline())
    for tmp in file:
        id, cost, stat = map(int, tmp.split())
        all_costs.append(cost)
        if id not in data:
            data[id] = [cost, stat]

        else:
            data[id].append(stat)

avg = sum(all_costs) / N
exp = dict()
cheap = dict()

for id in data:
    if data[id][0] > avg:
        exp[id] = data[id]
    else:
        cheap[id] = data[id]

sales_leader = sorted(exp, key=lambda x: (-exp[x][1:].count(0), -exp[x][0], exp[x][1:].count(1)))[0]

ans1 = exp[sales_leader][0] * data[sales_leader][1:].count(0)
ans2 = data[sales_leader][1:].count(1)

print(ans1, ans2)
