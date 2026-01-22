from itertools import combinations


def f(x):
    P = 66 <= x <= 67
    O = 32 <= x <= 125
    T = 30 <= x <= 491
    A = A1 <= x <= A2
    return (not A) <= (P or (not O) or (not T))


linea = [30, 32, 66, 67, 125, 491]
linex = [31, 52, 66.5, 100, 333]
ans = []
for A1, A2 in combinations(linea, 2):
    if all(f(x) for x in linex):
        ans.append(A2 - A1)
print(min(ans))
