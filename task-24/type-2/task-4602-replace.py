with open(r'..\files\24_4602.txt') as file:
    data = file.readline()
vow = 'AO'
con = 'BCD'

for i in vow:
    data = data.replace(i, '+')
for i in con:
    data = data.replace(i, '-')

data = data.replace('-+', '*')
for i in '+-':
    data = data.replace(i, ' ')

data = data.split()

print(len(max(data, key=len)))
