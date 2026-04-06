# def f(x):
#     x = sorted(x)
#     if all(x[i + 1] == x[i] + 1 for i in range(len(x) - 1)):
#         return True
#     return False
#
#
# with open('files/26 (1).txt') as file:
#     N = int(file.readline())
#     points = dict()
#     for i in file:
#         tmp = list(map(int, i.split()))[::-1]
#         if tmp[0] not in points:
#             points[tmp[0]] = [tmp[1]]
#         elif tmp[1] not in points[tmp[0]]:
#             points[tmp[0]].append(tmp[1])
# ans = []
# for key in points:
#     if f(points[key]):
#         ans.append([len(points[key]), key])
# ans.sort(key=lambda x: (-x[0], x[1]))
# print(*ans[0])


def f(data):
    res = 0
    data.sort()
    cnt = 0
    for i in range(len(data) - 1):
        if data[i + 1] == data[i] + 1:
            cnt += 1
            res = max(res, cnt)
        else:
            res = max(res, cnt)
            cnt = 0
    return res + 1


with open('files/26 (1).txt') as file:
    N = int(file.readline())
    points = dict()
    for i in file:
        tmp = list(map(int, i.split()))[::-1]
        if tmp[0] not in points:
            points[tmp[0]] = [tmp[1]]
        elif tmp[1] not in points[tmp[0]]:
            points[tmp[0]].append(tmp[1])

ans = []

for key in points:
    ans.append([f(points[key]), key])

ans.sort(key=lambda x: (-x[0], x[1]))
print(*ans[0])
