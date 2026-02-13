def f(n):
    if n < 3: return 1
    elif n % 2: return f(n - 2) + 2 * n - 2
    return f(n - 1) + n - 1
print(f(34))