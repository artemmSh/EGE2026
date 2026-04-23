from math import *


def center(cl):
    res = []
    for d in cl:
        sum_dist = sum(dist(d, p) for p in cl)
        res.append([sum_dist, d])
    return min(res)[1]


with open('files/27A_18625.txt') as file:
    file.readline()
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

cls = [[d for d in data if 1.5 < d[1] < - d[0] / 2 + 9 and d[0] < 8],
       [d for d in data if d not in [d for d in data if 1.5 < d[1] < - d[0] / 2 + 9 and d[0] < 8] and d[1] > 1.5]]

cls = [cl for cl in cls if len(cl) > 30]
centers = [center(cl) for cl in cls]

px = int(sum(c[0] for c in centers) / len(centers) * 100_000)
py = int(sum(c[1] for c in centers) / len(centers) * 100_000)

print(px, py)
