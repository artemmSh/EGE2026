def f(x):
    B = 70 <= x <= 80
    return (x % 12 == 0) and B and (x % A != 0)


cnt = 0
for A in range(1, 10000):
    if all(not f(x) for x in range(1, 1000)):
        cnt += 1
print(cnt)
