from functools import cache


@cache
def f(start, last_was_1=False, was_11=False):
    total = 0
    if start == 11: was_11 = True
    if start == 79 and was_11: return 1
    if start > 79 or start == 23: return 0
    if not last_was_1:
        total += f(start + 1, True, was_11)
    total += f(start + 2, False, was_11) + f(start * 2, False, was_11)
    return total


print(f(3))
