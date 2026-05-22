with open('files/26_9756.txt') as file:
    N = int(file.readline())
    requests = [list(map(int, i.split())) for i in file]

requests.sort(key=lambda x: (x[1]))
ans = [requests[0][1]]
for start, end in requests[1:]:
    if start >= ans[-1]:
        ans.append(end)
ans = ans[:-1]
for start, end in requests[::-1]:
    if start >= ans[-1]:
        ans.append(end)
        break
ans_1 = len(ans)
ans_2 = ans[-1]
print(ans_1, ans_2)
