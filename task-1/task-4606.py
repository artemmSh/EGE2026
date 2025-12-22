from itertools import permutations

matrix = '68 47 45 237 368 15 248 157'.split()
graph = 'AC CE EG GF FB BA FA CD DH HE'.split()
print(*range(1, 9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
