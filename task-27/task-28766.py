def min_max_yellow_supergiant_cnt(cls):
    res = []
    for cl in cls:
        cnt = sum(d[1][0] == 'Z' and d[1][-1] == 'I' and len(d[1]) == 3 for d in cl)
        res.append([cnt, cl])
    return min(res)[1], max(res)[1]


def center(cl):
    res = []
    for d in cl:
        sum_dist = sum(dist(d[0], p[0]) for p in cl)
        res.append([sum_dist, d])
    return min(res)[1]


from math import dist

with open('files/27_B_28766.txt') as file:
    data = [(list(map(float, i.replace(',', '.').split()[:-1])), i.split()[-1]) for i in file]

data_copy = data.copy()

clusters = list()
while data:
    clusters.append([data.pop()])
    for d in clusters[-1]:
        neigh = [n for n in data if dist(d[0], n[0]) < 1]
        clusters[-1].extend(neigh)
        for used in neigh: data.remove(used)

clusters.sort(key=len)

centers = [center(cl) for cl in clusters]

# print(int(min(dist(centers[0][0], d[0]) for d in data_copy if d[1][0] == 'Y' and d[1][-3:] == 'III') * 10_000), end=' ') -> 4940
# print(int(max(dist(centers[0][0], d[0]) for d in data_copy if d[1][0] == 'Y' and d[1][-3:] == 'III') * 10_000)) -> 74302

minimum, maximum = min_max_yellow_supergiant_cnt(clusters)

ans_1 = int(min(dist(d[0], p[0]) for cl in clusters for d in cl for p in cl if d[1][0] + p[1][0] == 'ZZ' and d[1][-1] + p[1][-1] == 'II' and len(d[1]) == 3 and len(p[1]) == 3 and dist(d[0], p[0]) > 0) * 10_000)
ans_2 = int(abs(dist(center(minimum)[0], center(maximum)[0]) * 10_000))

# print(ans_1, ans_2) -> 1035 125591