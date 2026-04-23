# from math import dist
#
#
# def center(cl):
#     res = []
#     for d in cl:
#         sum_dist = sum(dist(d, p) for p in cl)
#         res.append([sum_dist, d])
#     return min(res)[1]
#
#
# with open('files/27_A_28766.txt') as file:
#     dots = []
#     target = []
#     for i in file:
#         x, y, data = i.replace(',', '.').split()
#         dots.append(list(map(float, [x, y])))
#         if data[0] == 'Y' and data[-3:].strip() == 'III':
#             target.append(list(map(float, [x, y])))
#
# cl1 = [d for d in dots if d[1] < 8]
# cl2 = [d for d in dots if d[1] > 8]
# cls = [cl1, cl2]
# cls.sort(key=len)
# centers = [center(cl) for cl in cls]
# a1 = min(dist(centers[0], d) for d in target)
# a2 = max(dist(centers[0], d) for d in target)
# print(int(a1 * 10_000), int(a2 * 10_000))

from itertools import combinations
from math import dist


def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'.\files\27_B_28766.txt') as file:
    dots = []
    target = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Z' and data[2:].strip() == 'I':
            target.append(list(map(float, [x, y])))

cluster_1 = [
    [d for d in dots if d[1] < 15],
    [d for d in target if d[1] < 15]
]

cluster_2 = [
    [d for d in dots if 15 < d[1] < 22],
    [d for d in target if 15 < d[1] < 22]
]

cluster_3 = [
    [d for d in dots if 22 < d[1]],
    [d for d in target if 22 < d[1]]
]

B1 = 10 ** 10
clusters = [cluster_1, cluster_2, cluster_3]
for c in clusters:
    B1 = min([B1] + [dist(*d) for d in combinations(c[1], 2)])

min_cluster = center(min(clusters, key=lambda x: len(x[1]))[0])
max_cluster = center(max(clusters, key=lambda x: len(x[1]))[0])

B2 = dist(min_cluster, max_cluster)

print(B1 * 10_000, B2 * 10_000)
