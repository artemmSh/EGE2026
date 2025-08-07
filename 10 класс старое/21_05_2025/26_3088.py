

with open('26_3088.txt') as file:
    N = int(file.readline())
    menu = dict()
    for i in file:
        time, burger_id = map(int, i.split())
        if burger_id not in menu:
            menu[burger_id] = []
        menu[burger_id].append(time)
for i in menu:
    menu[i].sort()
ans2 = []
timeline = [0] * 961
for burger_id in menu:
    waiting = 0
    for i in range(0, len(menu[burger_id])-1, 2):
        start, end = menu[burger_id][i], menu[burger_id][i+1]
        waiting += end - start
        timeline[end] += 1
    if len(menu[burger_id]) > 1:
        waiting /= len(menu[burger_id]) // 2
        ans2.append([waiting, burger_id])
ans1 = 0
for i in range(961):
    ans1 = max(ans1, sum(timeline[i:i + 60]))
print(ans1, max(ans2)[1])