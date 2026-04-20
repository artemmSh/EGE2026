from math import dist


def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open('files/27_A_21599.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cl_a_1 = [d for d in dots if d[1] > 0.8 * d[0] - 8]
cl_a_2 = [d for d in dots if -7 < d[1] < 0.8 * d[0] - 8]
cl_a_3 = [d for d in dots if d[1] < - 7]

center_a_1 = center(cl_a_1)
center_a_2 = center(cl_a_2)
center_a_3 = center(cl_a_3)

print(int(abs(int(center_a_1[0] + center_a_2[0] + center_a_3[0]) / 3 * 10_000)), end=' ')
print(int(abs((center_a_1[1] + center_a_2[1] + center_a_3[1]) / 3 * 10_000)))

with open('files/27_B_21599.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cl_b_1 = [d for d in dots if d[1] < -5]
cl_b_2 = [d for d in dots if -5 < d[1] < d[0]]
cl_b_3 = [d for d in dots if d[0] < d[1] < 12 / 7 * d[0] + 12]
cl_b_4 = [d for d in dots if 12 / 7 * d[0] + 12 < d[1] and d[0] > 9]
cl_b_5 = [d for d in dots if -7 / 5 * d[0] - 84 / 5 < d[1] and d[0] < 9]
cl_b_6 = [d for d in dots if d[1] < -7 / 5 * d[0] - 84 / 5]
