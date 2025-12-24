with open('files/24_4710.txt') as file:
    data = file.readline()

for i in 'AO':
    data = data.replace(i, '+')
for i in 'CDF':
    data = data.replace(i, '-')
data = data.replace('-+', '*')
data = data.replace('-', ' ')
data = data.replace('+', ' ')
data = data.split()
print(len(max(data, key=len)))
