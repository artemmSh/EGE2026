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

cluster_A_1 = [d for d in data if d[0] < 5]
cluster_A_2 = [d for d in data if d[0] > 5]

center_A_1 = center(cluster_A_1)
center_A_2 = center(cluster_A_2)
print(max(center_A_1[0], center_A_2[0]) * 10_000)
print(max(center_A_1[1], center_A_2[1]) * 10_000)

with open('files/27_B_23209.txt') as file:
    file.readline()
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_B_1 = [d for d in data if 3 < d[1] < 12]
cluster_B_2 = [d for d in data if 15 < d[1] < 21]
cluster_B_3 = [d for d in data if 21 < d[1] < 27]

center_B_min = center(min(cluster_B_1, cluster_B_2, cluster_B_3, key=len))
center_B_max = center(max(cluster_B_1, cluster_B_2, cluster_B_3, key=len))
print((center_B_min[0] - center_B_max[0]) * 10_000)
print((center_B_min[1] - center_B_max[1]) * 10_000)
