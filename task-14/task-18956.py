from string import printable as alph

ans = 10 ** 10
for A in range(1, 1000000):
    for x in alph[:15]:
        M = int(f'432{x}3', 15)
        N = int(f'86{x}86', 15)
        if (M + A) % N == 0:
            ans = min(ans, A)
print(ans)
