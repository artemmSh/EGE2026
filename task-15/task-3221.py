#  руками решил ответ 55
def f(x):
    return ((x % 3 == 0) <= (x % 5)) and (x + A >= 70)


for A in range(1, 1_000_000):
    if all(f(x) for x in range(1, 1_000_000)):
        print(A)
        break
