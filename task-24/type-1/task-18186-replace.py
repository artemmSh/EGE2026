with open('../files/24_18186.txt') as file:
    data = file.readline()
vow = 'AE'
con = 'BCDFGH'
for i in vow:
    data = data.replace(i, 'v')
for i in con:
    data = data.replace(i, 'c')

data = data.replace('ccv', 'ccv ccv')
data = data.split()[1:-1]
print(len(max(data, key=len)))
