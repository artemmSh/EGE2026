import string

with open('../files/24_6757.txt') as file:
    data = file.readline()

combs = ['CFE', 'FCE']

for i in combs:
    data = data.replace(i, '*')

for i in string.ascii_uppercase:
    data = data.replace(i, ' ')

data = data.split()

print(len(max(data, key=len)))
