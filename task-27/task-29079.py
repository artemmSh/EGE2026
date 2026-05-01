from math import dist
from itertools import combinations


def ctr(cl):
    res = []
    for d in cl:
        sum_dist = sum(dist(d[0], p[0]) for p in cl)
        res.append([sum_dist, d])
    return min(res)[1]


with open('files/27_A_29079.txt') as file:
    data = [(list(map(float, i.replace(',', '.').split()[:-1])), i.split()[-1]) for i in file]

cls = [[d for d in data if d[0][1] > 10], [d for d in data if d[0][1] < 10]]

a1 = int(min(min(dist(ctr(cls[0])[0], d[0]) for d in cls[1] if d[1][0] == 'N' and d[1][-2:] == 'IV'), min(dist(ctr(cls[1])[0], d[0]) for d in cls[0] if d[1][0] == 'N' and d[1][-2:] == 'IV')) * 10_000)
a2 = int(max(max(dist(ctr(cls[0])[0], d[0]) for d in cls[1] if d[1][0] == 'N' and d[1][-2:] == 'IV'), max(dist(ctr(cls[1])[0], d[0]) for d in cls[0] if d[1][0] == 'N' and d[1][-2:] == 'IV')) * 10_000)

########################################################################################################################

with open('files/27_B_29079.txt') as file:
    data = [(list(map(float, i.replace(',', '.').split()[:-1])), i.split()[-1]) for i in file]

cls = [[d for d in data if d[0][1] > 23], [d for d in data if 15 < d[0][1] < 23], [d for d in data if d[0][1] < 15]]

cls.sort(key=len)

b1 = int(max(d[0][0] for d in cls[-1] if d[1][0] + d[1][-1] == 'JV' and len(d[1]) == 3) * 10_000)
b2 = int(max(d[0][1] for d in cls[0] if d[1][0] + d[1][-1] == 'JV'and len(d[1]) == 3) * 10_000)

print(a1, a2)
print(b1, b2)


