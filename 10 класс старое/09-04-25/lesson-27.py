with open('26_6056.txt') as file:
    N = int(file.readline())
    rings = list()
    for i in range(N):
        rings.append(int(file.readline()))

rings = sorted(rings, reverse = True)

previous_number = rings[0]
counter=1
for x in range(1, len(rings)-1):
    next_number = rings[x]
    if previous_number-next_number>=56:
        previous_number = next_number
        counter+=1
print(counter, '\n', previous_number)