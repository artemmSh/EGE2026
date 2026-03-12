from itertools import permutations

matrix = '247 148 467 123 68 358 13 256'.split()
graph = 'AH HB BF FG GE EA ED GD AC FC HC'.split()
print(*range(1, 9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)