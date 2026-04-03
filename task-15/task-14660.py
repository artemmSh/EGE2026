from itertools import combinations


def f(x):
    P = 16 <= x <= 84
    Q = 27 <= x <= 43
    A = A1 <= x <= A2
    return (A <= P) or Q


linea = [16, 27, 43, 84]
linex = [17, 28, 44]
ans = []
for A1, A2 in combinations(linea, 2):
    if all(f(x) for x in linex):
        ans.append(A2 - A1)
print(max(ans))
