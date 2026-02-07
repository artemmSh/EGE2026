with open('files/24_23381.txt') as file:
    data = file.readline()
ans = 0
for l in range(len(data)):
    if data[l] in '02468':
        for r in range(l + 1, len(data)):
            if data[r].isdigit():
                if data[r] in '02468' and all(data[l + 1:r].count(i) > 1 for i in data[l + 1:r]):
                    ans = max(ans, len(data[l:r + 1]))
                break
print(ans)
