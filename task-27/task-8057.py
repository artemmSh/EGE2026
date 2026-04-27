from math import dist


def ctr(cl):
    res = []
    for d in cl:
        sum_dist = sum(dist(d, p) for p in cl)
        res.append([sum_dist, d])
    return min(res)[1]


with open('files/27-94b.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

cls = []
while data:
    cls.append([data.pop()])
    for d in cls[-1]:
        neigh = [n for n in data if dist(d, n) < 0.23]
        cls[-1].extend(neigh)
        for used in neigh: data.remove(used)

cls = [cl for cl in cls if len(cl) > 30]

ctrs = [ctr(cl) for cl in cls]

px = int(100_000 * sum(ctr[0] for ctr in ctrs)/len(cls))
py = int(100_000 * sum(ctr[1] for ctr in ctrs)/len(cls))

print(px, py)