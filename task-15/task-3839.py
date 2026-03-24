def f(x):
    if A:
        return (A % 25 == 0) and ((x % 24 == 0) and (x % 75 == 0)) <= (x % A == 0)
    return 0


cnt = 0
for A in range(-5000, 5000):
    if all(f(x) for x in range(-5000, 5000)):
        cnt += 1
print(cnt)
