from importlib.metadata import pass_none
from math import dist


def ctr(cl):
    res = []
    for d in cl:
        sum_dist = sum(dist(d, p) for p in cl)
        res.append([sum_dist, d])
    return min(res)[1]


with open('files/27_A_28946.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

cls = [[d for d in data if d[1] > 15], [d for d in data if d[1] < 15]]
ctrs = [ctr(cl) for cl in cls]

a1 = int(sum(d[1] < ctr(max(cls, key=len))[1] for d in max(cls, key=len)))
a2 = int(abs(ctrs[0][0] - ctrs[1][0]) * 10_000)

with open('files/27_B_28946.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

cls = [[d for d in data if d[1] > 23], [d for d in data if d[1] < 23 and d[0] < 24], [d for d in data if d[0] > 24]]
cls.sort(key=len)
ctrs = [ctr(cl) for cl in cls]

b1 = sum((ctr(cls[0])[0] - 0.9 < d[0] < ctr(cls[0])[0] + 0.9) and (ctr(cls[0])[1] - 0.9 < d[1] < ctr(cls[0])[1] + 0.9) for d in cls[0])
b2 = int(abs(ctr(cls[1])[1] - ctr(cls[2])[1]) * 10_000)

print(a1, a2)
print(b1, b2)
