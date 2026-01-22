def triangle(n, m, k):
    return n + m > k and n + k > m and m + k > n


def f(x):
    return not ((triangle(x, 11, 18) == (not max(x, 5) > 68)) and triangle(x, A, 5))


for A in range(1000, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break
