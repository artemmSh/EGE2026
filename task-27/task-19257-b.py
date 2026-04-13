from math import dist


def center(cluster):
    ans = []
    for dot_1 in  cluster:
        sum_dist = sum(dist(dot_1, dot_2) for dot_2 in cluster)
        ans.append([sum_dist, dot_1])
    return min(ans)[1]


with open('files/19257-b.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_1 = [dot for dot in dots if dot[1] > 8]
cluster_2 = [dot for dot in dots if dot[1] < 5 and dot[0] > 0]
cluster_3 = [dot for dot in dots if dot[0] < 0]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)

print(int(abs((center_1[0] + center_2[0] + center_3[0]) / 3 * 10_000)), end=' ')
print(int(abs((center_1[1] + center_2[1] + center_3[1]) / 3 * 10_000)))
