with open('26_3377.txt') as file:
    N = int(file.readline())
    data = []
    for i in file:
        x,y = map(int, i.split())
        data.append([x, y])
print(data)