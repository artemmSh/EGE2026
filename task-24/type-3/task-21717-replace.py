with open('../files/24_21717.txt') as file:
    data = file.readline()

data = data.split('RSQ')
ans = 100 ** 100
eps = 130
for i in range(len(data) - eps):
    line = 'rsq'.join(data[i:i + eps + 1])
    line = line[line.find('rsq'):line.rfind('rsq') + 4]
    if line[-1] not in 'Qq':
        ans = min(ans, len(line))
print(ans)
