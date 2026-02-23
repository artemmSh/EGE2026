res = set()


def f(start, cnt):
    if cnt == 8 and 1000 <= start <= 1024: res.add(start)
    elif cnt > 8: return
    else:
        f(start + 1, cnt + 1)
        f(start + 5, cnt + 1)
        f(start * 3, cnt + 1)
f(1, 0)
print(len(res))