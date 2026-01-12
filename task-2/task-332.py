from itertools import *


def f(w, x, y, z):
    return (x or y and not z) and not w


table = [
    (1, 0, 0, 0),
    (0, 0, 1, 0),
    (0, 1, 0, 1)
]
if len(table) == len(set(table)):
    for p in permutations('wxyz'):
        if [f(**dict(zip(p, t))) for t in table] == [1, 1, 0]:
            print(*p)
