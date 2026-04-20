from math import dist


def edge(cl):
    res = []
    for d in cl:
        sum_dist = sum(dist(d, p) for p in cl)
        res.append([sum_dist, d])
    return max(res)[1]


with open('files/27.17.B_19566.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

clusters = list()
while data:
    clusters.append([data.pop()])
    for d in clusters[-1]:
        neigh = [n for n in data if dist(d, n) < 2]
        clusters[-1].extend(neigh)
        for used in neigh: data.remove(used)

clusters = [cl for cl in clusters if len(cl) > 30]
edges = [edge(cl) for cl in clusters]

print(int(abs(sum(e[0] for e in edges) / len(clusters) * 10_000)), end=' ')
print(int(abs(sum(e[1] for e in edges) / len(clusters) * 10_000)))
