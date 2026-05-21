with open('../files/24-280.txt') as file:
    data = file.readline()

for i in 'XY':
    data = data.replace(i, ' ')

data = data.split()
ans = 0
for line in data:
    cnt_s = cnt_u = cnt_n = 0
    l = 0
    for r in range(len(line)):
        if line[r] == 'S': cnt_s += 1
        if line[r] == 'U': cnt_u += 1
        if line[r] == 'N': cnt_n += 1
        while max(cnt_s, cnt_u, cnt_n) > 10:
            if line[l] == 'S': cnt_s -= 1
            if line[l] == 'U': cnt_u -= 1
            if line[l] == 'N': cnt_n -= 1
            l += 1
        ans = max(ans, r - l + 1)

print(ans)
