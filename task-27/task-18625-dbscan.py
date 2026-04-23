from math import *


def center(cl):
    res = []
    for d in cl:
        sum_dist = sum(dist(d, p) for p in cl)
        res.append([sum_dist, d])
    return min(res)[1]


with open('files/27B_18625.txt') as file:
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
centers = [center(cl) for cl in cls]

px = int(sum(c[0] for c in centers) / len(centers) * 100_000)
py = int(sum(c[1] for c in centers) / len(centers) * 100_000)

print(px, py)
