from math import dist

with open('files/27.21.B_19715.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]


def center(cl):
    res = []
    for d in cl:
        sum_dist = sum(dist(d, p) for p in cl)
        res.append([sum_dist, d])
    return min(res)[1]


clusters = list()
while data:
    clusters.append([data.pop()])
    for d in clusters[-1]:
        neigh = [n for n in data if dist(d, n) < 5]
        clusters[-1].extend(neigh)
        for used in neigh: data.remove(used)

clusters = [cl for cl in clusters if len(cl) > 30]

centers = [center(cl) for cl in clusters]

# print(int(abs(sum(c[0] for c in centers) / 2 * 10_000)), end=' ')
# print(int(abs(sum(c[1] for c in centers) / 2 * 10_000)))

print(int(abs(sum(c[0] for c in centers) / 4 * 10_000)), end=' ')
print(int(abs(sum(c[1] for c in centers) / 4 * 10_000)))
