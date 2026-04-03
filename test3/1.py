from itertools import permutations

matrix = '457 567 45 136 123 247 126'.split()
graph = 'AB BG GE EF FA FD AD EC CD EC CB'.split()
print(*range(1, 8))
for p in permutations('ABCDEFG'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)
