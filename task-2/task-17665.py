from itertools import *


def f(w, x, y, z):
    return (z <= (not (y <= x))) or w


for x1, x2, x3, x4, x5, x6, x7 in product((0, 1), repeat=7):
    t = (
        (x1, 1, x2, x3, 0),
        (x4, x5, 0, 0, 0),
        (x6, 0, 1, x7, 0)
    )
    if len(t) == len(set(t)):
        for p in permutations('wxyz'):
            if all(f(**dict(zip(p, i))) == i[-1] for i in t):
                print(*p, sep='')
