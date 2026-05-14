with open('../files/24_8510.txt') as file:
    data = file.readline()

forbidden = [i + j for i in 'NOP' for j in 'NOP']
for f in forbidden:
    data = data.replace(f, f'{f[0]} {f[1]}')
data = data.split()
print(len(max(data, key=len)))
