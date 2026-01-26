with open('files/24_13715.txt') as file:
    data = file.readline()

cnt = 0
ans = 0
for i in range(len(data) - 1):
    if data[i:i + 2] == 'AB':
        cnt = 1
        for j in range(i + 2, len(data) - 1):
            if data[j:j + 2] == 'AB':
                cnt += 1
            if cnt == 51:
                ans = max(ans, len(data[i:j + 1]))
print(ans)
