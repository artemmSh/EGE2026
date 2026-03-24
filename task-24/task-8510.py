with open('files/24_8510.txt') as file:
    data = file.readline()

data = data.replace('N', '*').replace('O', '*').replace('P', '*')
data = data.split('*')

if data.index(max(data, key=len)) not in (0, len(data) - 1):
    print(len(max(data, key=len)) + 2)
else:
    print(len(max(data, key=len)) + 1)
