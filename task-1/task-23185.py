from itertools import *

print(*range(1, 9))
matrix = '478 38 256 15 34 37 168 127'.split()
graph = 'AH HF FE ED DG GA GC CB BH BF'.split()
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
print(34 + 11)
