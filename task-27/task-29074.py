from math import dist


def center(cl):
    res = []
    for d in cl:
        sum_dist = sum(dist(d[0], p[0]) for p in cl)
        res.append([sum_dist, d])
    return min(res)[1]


with open('files/27_A_29074.txt') as file:
    data = [(list(map(float, i.replace(',', '.').split()[:-1])), i.split()[-1]) for i in file]

cls = [[d for d in data if d[0][1] > 10], [d for d in data if d[0][1] < 10]]

a1 = int(min(sum(d[1][0] == 'Z' for d in cl) for cl in cls))
a2 = int(max(sum(d[1][0] == 'Z' for d in cl) for cl in cls))
centers = [center(cl) for cl in cls]
b1 = int(min(dist(centers[i][0], d[0]) for i in range(len(cls)) for d in cls[i] if d[1][0] == 'L' and d[1][-1] == 'V') * 10_000)
b2 = int(max(dist(centers[i][0], d[0]) for i in range(len(cls)) for d in cls[i] if d[1][0] == 'L' and d[1][-1] == 'V') * 10_000)

print(a1, a2)
print(b1, b2)