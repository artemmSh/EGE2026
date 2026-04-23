from math import dist


def clusterization(data):
    cls = list()
    while data:
        cls.append([data.pop()])
        for d in cls[-1]:
            neigh = [n for n in data if dist(d, n) < 2]
            cls[-1].extend(neigh)
            for used in neigh: data.remove(used)
    return [cl for cl in cls if len(cl) > 30]


def center(cl):
    res = []
    for d in cl:
        sum_dist = sum(dist(d, p) for p in cl)
        res.append([sum_dist, d])
    return min(res)[1]


def q2():
    res = []
    for i in range(len(cls)):
        for d in cls[i]:
            tmp = cls.copy()
            tmp.remove(cls[i])
            sum_dist = sum(dist(d, p) for p in tmp[0] + tmp[1])
            res.append([sum_dist, d])
    return max(res)[1]


with open('files/27A_27138.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

cls = clusterization(data)
centers = [center(cl) for cl in cls]

sx = int(abs(centers[0][0] - centers[1][0]) * 10_000)
sy = int(abs(centers[0][1] - centers[1][1]) * 10_000)

with open('files/27B_27138.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

cls = clusterization(data)
cls.sort(key=len)
q1 = int(abs(max(d[0] for d in cls[1])) * 10_000)
q2 = int(abs(sum(q2())) * 10_000)

print(sx, sy)
print(q1, q2)
