from math import dist
from itertools import combinations


def ctr(cl):
    res = []
    for d in cl:
        sum_dist = sum(dist(d[0], p[0]) for p in cl)
        res.append([sum_dist, d])
    return min(res)[1]


with open('files/27_A_29081.txt') as file:
    data = [(list(map(float, i.replace(',', '.').split()[:-1])), i.split()[-1]) for i in file]

cls = [[d for d in data if d[0][1] > 10], [d for d in data if d[0][1] < 10]]

a1 = int(min(dist(d[0], ctr(cl)[0]) for cl in cls for d in cl if d[1][-3:] == 'VII') * 10_000)
a2 = int(max(dist(d[0], ctr(cl)[0]) for cl in cls for d in cl if d[1][-3:] == 'VII') * 10_000)

########################################################################################################################

with open('files/27_B_29081.txt') as file:
    data = [(list(map(float, i.replace(',', '.').split()[:-1])), i.split()[-1]) for i in file]

cls = [[d for d in data if d[0][1] > 23], [d for d in data if 15 < d[0][1] < 23], [d for d in data if d[0][1] < 15]]

b1 = int(min(dist(d1[0], d2[0]) for duo in combinations(cls, 2) for d1 in duo[0] for d2 in duo[1] if d1[1][1] in '89' and d2[1][1] in '89') * 10_000)
b2 = [dist(d1[0], d2[0]) for cl in cls for d1 in cl for d2 in cl if d1[1][1] in '89' and d2[1][1] in '89' and d1 != d2]
b2 = int(10_000 * sum(b2) / len(b2))

print(a1, a2)
print(b1, b2)

