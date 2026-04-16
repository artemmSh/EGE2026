from math import dist

with open('files/27_B_17834.txt') as file:
    file.readline()
    data = [list(map(float, i.replace(',', '.').split())) for i in file]


def center(cl):
    res = []
    for d in cl:
        sum_dist = sum(dist(d, n) for n in cl)
        res.append([sum_dist, d])
    return min(res)[1]


clusters = list()
while data:
    clusters.append([data.pop(0)])
    for d in clusters[-1]:
        neighbours = [n for n in data if dist(d, n) < 1]
        clusters[-1].extend(neighbours)
        for used in neighbours: data.remove(used)

centers = [center(cl) for cl in clusters]

# print(int(sum(c[0] for c in centers) / 2 * 100), end=' ')
# print(int(sum(c[1] for c in centers) / 2 * 100))

print(int(sum(c[0] for c in centers) / 3 * 100), end=' ')
print(int(sum(c[1] for c in centers) / 3 * 100))
