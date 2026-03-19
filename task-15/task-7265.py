def f(x):
    return ((x % 2 == 0) <= (x % 3)) or ((x + A) >= 100)


for A in range(1, 50_000):
    if all(f(x) for x in range(1, 100_000)):
        print(A)
        break
