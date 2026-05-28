with open('files/26_23283.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]
data.sort()
windows = [0] * K
cnt = 0
last = 0
for cus in data:
    for w in range(len(windows)):
        if cus[0] > windows[w]:
            windows[w] = cus[1]
            cnt += 1
            last = w + 1
            break
print(cnt, last)
