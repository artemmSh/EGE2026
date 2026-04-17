with open('files/26_21424.txt') as file:
    N = int(file.readline())
    data = [int(i) for i in file]

data.sort(reverse=True)

ans = [data[0]]
for box in data[1:]:
    if ans[-1] - box >= 9:
        ans.append(box)
print(len(ans), ans[-1])
