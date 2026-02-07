with open('files/24_23206 (1).txt') as file:
    data = file.readline()
for i in '02468':
    data = data.replace(i, '*')
ans = 0
for l in range(len(data)):
    if data[l] == '*':
        cnt = 0
        for r in range(l + 1, len(data)):
            if data[r] == 'S':
                cnt += 1
            if data[r] == '*':
                if cnt == 35:
                    ans = max(ans, len(data[l:r]))
                break
            if cnt == 36:
                ans = max(ans, len(data[l:r]))
                break
print(ans)
