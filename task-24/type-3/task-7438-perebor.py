with open('../files/24-293.txt') as file:
    data = file.readline()

for i in '0123456789':
    data = data.replace(i, '0')

m = 0
for l in range(len(data)):
    for r in range(l + m, len(data)):
        line = data[l:r + 1]
        if line.count('D') > 100: break
        if 'DS' in line or 'SD' in line: break
        if '0' in line: break
        m = max(m, len(line))
print(m)
