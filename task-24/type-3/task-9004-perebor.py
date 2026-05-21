with open('../files/24-384.txt') as file:
    data = file.readline()

m = 10000
for l in range(len(data)):
    for r in range(l + m, l, -1):
        line = data[l:r + 1]
        if line.count('Z') < 270: break
        m = min(m, len(line))
print(m)
