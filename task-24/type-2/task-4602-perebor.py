with open(r'..\files\24_4602.txt') as file:
    data = file.readline()
vow = 'AO'
con = 'BCD'

ans = 0

for i in range(len(data) - 1):
    if data[i] in con and data[i + 1] in vow:
        cnt = 1
        for j in range(i + 2, len(data) - 1, 2):
            if data[j] in con and data[j + 1] in vow:
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
print(ans)
