def porch_info(x):
    tmp = x.copy()
    x = sorted(x)
    cnt = 1
    ans = []
    for k in range(len(x) - 1):
        if x[k + 1] == x[k] + 1:
            cnt += 1
        else:
            cnt = 1
        ans.append([cnt, k - cnt + 1])
    ans.sort(reverse=True)
    return ans[0][0], tmp[x[ans[0][1]]][0], x[ans[0][1]]


with open('files/26_24897.txt') as file:
    N = int(file.readline())
    houses = dict()
    for i in file:
        request, house, porch = map(int, i.split())
        if house not in houses:
            houses[house] = {porch: [request]}
        else:
            if porch not in houses[house]:
                houses[house][porch] = [request]
            else:
                houses[house][porch].append(request)

houses_copy = houses.copy()
houses = sorted(houses, key=lambda z: (-porch_info(houses[z])[0], porch_info(houses[z])[1]))
print(houses[0], porch_info(houses_copy[houses[0]])[2])
