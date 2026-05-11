with open(r'..\files\24_7600.txt') as file:
    data = file.readline()

forbidden = list()
for a in 'QRS':
    for b in 'QRS':
        forbidden.append(a + b)

for i in forbidden:
    data = data.replace(i, '* *')

data = data.split()

print(len(max(data, key=len)))
