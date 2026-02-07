with open('files/24_3792.txt') as file:
    data = file.readline()

ok = 'ABC'
no = 'DE'
for i in no:
    data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))
