def f(x):
    B = 50 <= x <= 70
    return (x % A == 0) or (B <= (not x % 16 == 0))


for A in range(5000, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break
