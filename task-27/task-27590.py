def anti_center(cl):
    res = []
    for d in cl:
        sum_dist = sum(dist(d, p) for p in cl)
        res.append([sum_dist, d])
    return max(res)[1]


from math import dist

with open('files/27B_27590.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

clusters = list()
while data:
    clusters.append([data.pop()])
    for d in clusters[-1]:
        neigh = [n for n in data if dist(d, n) < 1]
        clusters[-1].extend(neigh)
        for used in neigh: data.remove(used)

clusters = [cl for cl in clusters if len(cl) > 30]
clusters.sort(key=len)
anti_centers = [anti_center(cl) for cl in clusters]

# print(abs(int(sum(anti_centers[0]) * 10_000)), end=' ')
# print(abs(int(sum(anti_centers[-1]) * 10_000)))

anti_centers.sort(key=lambda x: (dist(x, [0, 0])))
print(abs(int(anti_centers[-1][0] * 10_000)), end=' ')
print(abs(int(anti_centers[0][1] * 10_000)))
