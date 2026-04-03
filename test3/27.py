from math import dist

with open('files/27_B.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

clusters = []
while data:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        neighbours = [n for n in data if dist(p, n) < 1]
        clusters[-1].extend(neighbours)
        for used in neighbours: data.remove(used)


def c(cl):
    ans = []
    for p in cl:
        ans.append([sum(dist(p, d) for d in cl), p])
    ans.sort()
    return ans[0]


centers = [c(cl) for cl in clusters]
# point = [-1.0, 1.3]
# print(len(min(clusters, key=len)), int(10_000 * sum(dist(center[1], point) for center in centers)))  -> 301 319272
for cl in clusters:
    if len(cl) == 200:
        print(sum(p != c(cl)[1] and dist(p, c(cl)[1]) <= 1.6 for p in cl))
    # if len(cl) == 902:
    #     print(int(10_000 * max(dist(p, c(cl)[1]) for p in cl)))
    #     break
