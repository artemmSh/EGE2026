with open('files/24_25361.txt') as file:
    data = file.readline()

cnt = 0
ans = 0
for i in range(len(data)):
    if data[i] in '02468':
        cnt = 0
        for j in range(i + 1, len(data)):
            if data[j] in '02468':
                break
            if data[j] == 'F':
                cnt += 1
            if cnt == 77:
                ans = max(ans, len(data[i:j + 1]) - 1)
                break

print(ans)
