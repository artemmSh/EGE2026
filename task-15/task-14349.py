from itertools import combinations


def f(x):
    B = 54 <= x <= 120
    C = 78 <= x <= 151
    A = A1 <= x <= A2
    return C <= ((B and (not A)) <= (not C))


linea = [54, 78, 120, 151]
linex = [60, 90, 130]
ans = []
for A1, A2 in combinations(linea, 2):
    if all(f(x) for x in linex):
        ans.append(A2 - A1)
print(min(ans))
