from itertools import *


def f(w, x, y, z):
    return (not (w <= (x == y))) and (z <= x)


for x1, x2, x3, x4, x5 in product((0, 1), repeat=5):
    t = (
        (x1, 0, 1, 0, 1),
        (0, x2, x3, 0, 1),
        (x4, 1, 1, x5, 1)
    )
    if len(t) == len(set(t)):
        for p in permutations('wxyz'):
            if all(f(**dict(zip(p, i))) == i[-1] for i in t):
                print(*p, sep='')
