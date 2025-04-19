with open('26_3664.txt') as file:
    N = int(file.readline())
    trees = list()
    for i in file:
        row, col = map(int, i.split())
        trees.append([row, col])
trees.sort()

max_row = 0
quantity = 0
maximum = 0
for i in range(N-1):
    first, second = trees[i], trees[i+1]
    if first[0] == second[0] and abs(first[1]-second[1])>maximum:
        maximum = abs(first[1]-second[1])
        max_row = trees[i][0]
print(max_row, maximum-1)
