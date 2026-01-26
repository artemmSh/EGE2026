with open('files/24_11667.txt') as file:
    data = file.readline()

cnt = 0
ans = 0
for i in range(len(data) - 7):
    if data[i:i + 8] == 'INFINITY':
        cnt = 1
        for j in range(i + 8, len(data) - 7):
            if data[j:j + 8] == 'INFINITY':
                cnt += 1
            if cnt == 1001:
                ans = max(ans, len(data[i:j + 7]))
print(ans)
