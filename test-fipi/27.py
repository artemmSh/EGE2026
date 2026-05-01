from math import dist


def ctr(cl):
    res = []
    for d in cl:
        sum_dist = sum(dist(d[0], p[0]) for p in cl)
        res.append([sum_dist, d])
    return min(res)[1]


with open('files/1_27_A.txt') as file:
    data = [(list(map(float, i.replace(',', '.').split()[:-1])), i.split()[-1]) for i in file]

cls = [[d for d in data if d[0][1] > 15], [d for d in data if d[0][1] < 15]]

cls.sort(key=len)
ctrs = [ctr(cl) for cl in cls]

ax = int(abs(min((dist(d[0], ctrs[0][0]), d[0]) for d in data if d[1][0] + d[1][-3:] == 'MIII')[1][0] * 10_000))
ay = int(abs(min((dist(d[0], ctrs[0][0]), d[0]) for d in data if d[1][0] + d[1][-3:] == 'MIII')[1][1] * 10_000))

with open('files/1_27_B.txt') as file:
    data = [(list(map(float, i.replace(',', '.').split()[:-1])), i.split()[-1]) for i in file]

cls = [[d for d in data if d[0][1] < 30], [d for d in data if d[0][0] > 16 and d[0][1] > 30], [d for d in data if d[0][0] < 16 and d[0][1] > 30]]

b1 = int(dist(ctr(min((sum(d[1][0] + d[1][-3:] == 'KIII' for d in cl), cl) for cl in cls)[1])[0], ctr(max((sum(d[1][0] + d[1][-3:] == 'KIII' for d in cl), cl) for cl in cls)[1])[0]) * 10_000)
b2 = int(max(dist(d1[0], d2[0]) for cl in cls for d1 in cl for d2 in cl if d1[1][0] + d1[1][-1] + d2[1][0] + d2[1][-1] == 'GVGV' and len(d1[1]) + len(d2[1]) == 6) * 10_000)

print(ax, ay)
print(b1, b2)


