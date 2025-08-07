with open('26_17565.txt') as file:
    N, S = map(int, file.readline().split())
    sailors = dict()
    for i in file:
        sailor = list(map(int, i.split()))
        sailors[sailor[0]] = (sum(sailor[1:-1]), sailor[-1])

sailors2 = sorted(sailors, key=lambda sailor_id: (sailors[sailor_id], -sailor_id), reverse=True)

last_passed = sailors2[S-1]
first_not_passed = sailors2[S]
half_point = 0
if sailors[last_passed][0] == sailors[first_not_passed][0]:
    half_point = sailors[last_passed][0]
counter = 0
for i in sailors:
    if sailors[i][0] == half_point:
        counter+=1
last_sailor_id = 0
sorted_sailors = dict()
for j in sailors2:
    sorted_sailors[j] = sailors[j]
for x in sorted_sailors:
    while sorted_sailors[x][0]> half_point:
        last_sailor_id = x
        break
print(last_sailor_id, counter)




