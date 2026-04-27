from itertools import combinations
from math import *


def ctr(cl):
    res = []
    for d in cl:
        sum_dist = sum(dist(d[0], p[0]) for p in cl)
        res.append([sum_dist, d])
    return min(res)[1]


with open('files/27_A_29075.txt') as file:
    data = [(list(map(float, i.replace(',', '.').split()[:-1])), i.split()[-1]) for i in file]

cls = [[d for d in data if d[0][1] > 10], [d for d in data if d[0][1] < 10]]

a1 = int(ctr(min((sum(d[1][-3:] == 'III' for d in cl), cl) for cl in cls)[1])[0][0] * 10_000)
a2 = int(ctr(max((sum(d[1][-3:] == 'III' for d in cl), cl) for cl in cls)[1])[0][1] * 10_000)

########################################################################################################################

with open('files/27_B_29075.txt') as file:
    data = [(list(map(float, i.replace(',', '.').split()[:-1])), i.split()[-1]) for i in file]

cls = [[d for d in data if d[0][1] > 23], [d for d in data if 15 < d[0][1] < 23], [d for d in data if d[0][1] < 15]]

b1 = int(min(dist(d1[0], d2[0]) for duo in combinations(cls, 2) for d1 in duo[0] for d2 in duo[1] if d1[1][0] + d2[1][0] == 'JJ') * 10_000)
b2 = int(max(dist(d1[0], d2[0]) for duo in combinations(cls, 2) for d1 in duo[0] for d2 in duo[1] if d1[1][0] + d2[1][0] == 'JJ') * 10_000)

print(a1, a2)
print(b1, b2)