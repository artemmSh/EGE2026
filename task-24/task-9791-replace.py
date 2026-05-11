from string import printable

with open('files/24_9791.txt') as file:
    data = file.readline().lower()

for i in printable[16:]:
    data = data.replace(i, ' ')

data = data.split()
print(len(max(data, key=len)))
