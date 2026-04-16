from math import dist


def center(cl):
    res = []
    for d in cl:
        sum_dist = sum(dist(d, p) for p in cl)
        res.append([sum_dist, d])
    return min(res)[1]


with open('files/27_A_23209.txt') as file:
    file.readline()
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 1
clusters = []
while data:
    cl = [data.pop()]
    for d in cl:
        for p in data.copy():
            if dist(d, p) < eps:
                cl.append(p)
                data.remove(p)
    if len(cl) > 30:
        clusters.append(cl)

centers = [center(cl) for cl in clusters]

print(max(centers, key=lambda x: x[0])[0] * 10_000)
print(max(centers, key=lambda x: x[1])[1] * 10_000)

with open('files/27_B_23209.txt') as file:
    file.readline()
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 1
clusters = []
while data:
    cl = [data.pop()]
    for d in cl:
        for p in data.copy():
            if dist(d, p) < eps:
                cl.append(p)
                data.remove(p)
    if len(cl) > 30:
        clusters.append(cl)

centers = [center(cl) for cl in clusters]

center_B_min = center(min(clusters, key=len))
center_B_max = center(max(clusters, key=len))
print((center_B_min[0] - center_B_max[0]) * 10_000)
print((center_B_min[1] - center_B_max[1]) * 10_000)
