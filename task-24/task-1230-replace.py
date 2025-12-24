with open('files/24_1230.txt') as file:
    data = file.readline()

for i in 'WRQ':
    data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))
