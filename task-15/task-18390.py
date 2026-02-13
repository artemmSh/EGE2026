from itertools import combinations


def f(x):
    P = 10 <= x <= 150
    Q = 160 <= x <= 250
    R = 240 <= x <= 300
    A = A1 <= x <= A2
    return (Q <= P) or ((not A) <= R)


linea = [10, 150, 160, 240, 250, 300]
linex = [11, 151, 161, 241, 251]
ans = []
for A1, A2 in combinations(linea, 2):
    if all(f(x) for x in linex):
        ans.append(A2 - A1)
print(min(ans))
