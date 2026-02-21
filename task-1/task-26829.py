from itertools import permutations

matrix = '248 137 268 15 467 357 256 13'.split()
graph = 'ГБ БЖ ЖЕ ЕВ ВД ДГ КБ КГ КА ЕА ДА'.split()
print(*range(1, 9))
for i in permutations('АБВГДЕЖК'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
