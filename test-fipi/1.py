from itertools import permutations

matrix = '27 1567 67 5 246 2357 1236'.split()
graph = 'ab bv bd vd vg dk ve de ge ke'.split()
print(*range(1, 8))
for i in permutations('abvgdek'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

print(9)
