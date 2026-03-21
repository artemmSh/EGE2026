with open('files/26.2_19727.txt') as file:
    M, N = map(int, file.readline().split())
    cans = [int(i) for i in file]

cans.sort()
ans = []
for can in cans:
    if sum(ans) + can <= M:
        ans.append(can)

free_space = M - sum(ans[:-1])
print(len(ans), sum(i > free_space for i in cans))
