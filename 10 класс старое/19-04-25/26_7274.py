with open('26_7274.txt') as file:
    N = int(file.readline())
    trees = []
    for i in file:
        row, col = map(int, i.split())
        trees.append([row, col])
trees.sort()
counter = 0
max_row = 0
min_col = 0
for i in range(N-1):
    first, second = trees[i], trees[i+1]
    if first[0] == second[0] and second[1] - first[1] - 1 == 13:
        max_row = trees[i][0]
        min_col = trees[i][1]+1
print(max_row, min_col)


