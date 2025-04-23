with open('26_17786.txt') as file:
    N, V = map(int, file.readline().split())
    V *= 1000
    weight = list()
    for i in file:
        weight.append(int(i))

weight.sort(reverse=True)
counter = 0
smallest = 0

for i in weight:
    if 7000 <= i <= 12000 and i <= V:
        V -= i
        counter += 1
        smallest = i

print(counter, smallest)
