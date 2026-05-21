with open('../files/24-371.txt') as file:
    data = file.readline()

m = 0
cnt_M = 0
for l in range(len(data)):
    if data[l] == 'M': cnt_M -= 1
    for r in range(l + m, len(data)):
        if data[r] == 'M': cnt_M += 1
        line = data[l:r + 1]
        if cnt_M > 112: break
        if line.count('.') > 1: break
        if cnt_M == 112 and line[-1] == '.':
            m = max(m, len(line))
print(m)
