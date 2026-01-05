from itertools import *


def f(w, x, y, z):
    return not (x <= y) or (z == w) or z


for i in product((0, 1), repeat=7):
    table = [
        (0, 0, i[0], i[1]),
        (i[2], i[3], 1, i[4]),
        (i[5], 1, 0, i[6])
    ]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
                print(*p, sep='')
