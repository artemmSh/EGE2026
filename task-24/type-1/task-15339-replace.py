with open('../files/24_15339.txt') as file:
    data = file.readline()

for i in 'ABC':
    data = data.replace(i, '*')
for i in '6789':
    data = data.replace(i, '$')

while '$$' in data or '**' in data:
    data = data.replace('$$', '$ $').replace('**', '* *')

data = data.split()

print(len(max(data, key=len)))
