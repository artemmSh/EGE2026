from math import dist
from itertools import combinations


def ctr(cl):
    res = []
    for d in cl:
        sum_dist = sum(dist(d, p) for p in cl)
        res.append([sum_dist, d])
    return min(res)[1]


with open('files/27_A_23284.txt') as file:
    file.readline()
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

cls = list()
while data:
    cls.append([data.pop()])
    for d in cls[-1]:
        neigh = [n for n in data if dist(d, n) < 1]
        cls[-1].extend(neigh)
        for used in neigh: data.remove(used)

cls = [cl for cl in cls if len(cl) > 30]

ctrs = [ctr(cl) for cl in cls]

px = abs(int(sum(c[0] for c in ctrs) * 10_000))
py = abs(int(sum(c[1] for c in ctrs) * 10_000))

with open('files/27_B_23284.txt') as file:
    file.readline()
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

cls = list()
while data:
    cls.append([data.pop()])
    for d in cls[-1]:
        neigh = [n for n in data if dist(d, n) < 1]
        cls[-1].extend(neigh)
        for used in neigh: data.remove(used)

cls = [cl for cl in cls if len(cl) > 30]

ctrs = [ctr(cl) for cl in cls]

q1 = abs(int(min(dist(c1, c2) for c1, c2 in combinations(ctrs, 2)) * 10_000))
q2 = abs(int(max(dist(c1, c2) for c1, c2 in combinations(ctrs, 2)) * 10_000))

print(px, py)
print(q1, q2)
