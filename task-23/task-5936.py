from functools import cache


@cache
def f(start, end, cnt=0):
    if start % 2: cnt += 1
    if start == end and cnt < 5: return 1
    if start > end: return 0
    return f(start + 2, end, cnt) + f(start + 3, end, cnt) + f(start * 2 + 1, end, cnt)


print(f(1, 625))
