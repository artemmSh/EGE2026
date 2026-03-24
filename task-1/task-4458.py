from itertools import permutations

matrix = '45 345 256 127 123 37 46'.split()
graph = 'AG GF FB BD DE EA CB CD CG'.split()
print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
