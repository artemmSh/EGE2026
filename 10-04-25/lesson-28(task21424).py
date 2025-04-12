from itertools import count

with open('26_21424.txt') as file:
    N = int(file.readline())
    sizes = [int(i) for i in file]

sizes.sort(reverse = True)

last = sizes[0]
counter = 1

for i in sizes:
    if last - 9 >= i:
        counter+=1
        last = i
print(counter, last)
