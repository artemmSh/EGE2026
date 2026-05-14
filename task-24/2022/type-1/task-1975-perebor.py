with open(r'..\..\files\24_1975.txt') as file:
    data = file.readline()

ans = 0
cnt = 1
for i in range(len(data) - 1):
    if data[i:i + 2] != 'PP':
        cnt += 1
    else:
        cnt = 1
    ans = max(ans, cnt)

print(ans)
