def f(x, c=0):
    if c == 13:
        res.add(x)
    else:
        f(x - 3, c + 1)
        f(x * (- 3), c + 1)


res = set()
f(333)
print(len([x for x in res if x < 0]))
