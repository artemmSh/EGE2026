with open('files/24_10105.txt') as file:
    data = file.readline()

ans = 0
for i in range(len(data)):
    if data[i] == 'T':
        cnt_T = 1
        for j in range(i + 1, len(data)):
            if data[j] == 'T':
                cnt_T += 1
            if cnt_T == 101:
                ans = max(ans, len(data[i:j]))
                break
print(ans)
