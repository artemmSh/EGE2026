from math import dist


def center(cl):
    res = []
    for d in cl:
        sum_dist = sum(dist(d, p) for p in cl)
        res.append([sum_dist, d])
    return min(res)[1]


with open('files/27B_18678.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

clusters = list()
while data:
    clusters.append([data.pop()])
    for d in clusters[-1]:
        neigh = [n for n in data if dist(d, n) < 1]
        clusters[-1].extend(neigh)
        for used in neigh: data.remove(used)

clusters = [cl for cl in clusters if len(cl) > 30]

centers = [center(cl) for cl in clusters]

# print(int(sum(c[0] for c in centers) / 2 * 100_000), end=' ')
# print(int(sum(c[1] for c in centers) / 2 * 100_000))

print(int(sum(c[0] for c in centers) / 3 * 100_000), end=' ')
print(int(sum(c[1] for c in centers) / 3 * 100_000))
