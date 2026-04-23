from math import *


def center(cl):
    res = []
    for d in cl:
        sum_dist = sum(dist(d, p) for p in cl)
        res.append([sum_dist, d])
    return min(res)[1]


with open('files/27A_18677.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

cls = [[d for d in data if d[0] - 4 < d[1] < d[0] * 5 / 4 - 1], [d for d in data if d[0] - 8 < d[1] < d[0] - 4]]

centers = [center(cl) for cl in cls]

px = int(sum(c[0] for c in centers) / len(centers) * 100_000)
py = int(sum(c[1] for c in centers) / len(centers) * 100_000)

print(px, py)
