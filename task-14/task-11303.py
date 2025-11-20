from string import printable as alph

for x in alph[:20]:
    N1 = int(f'627{x}j8', 20)
    N2 = int(f'h45i{x}5hij', 20)
    N3 = int(f'4idb49j{x}7', 20)
    N = N1 + N2 + N3
    if N % 19 == 0:
        print(x, N // 19)
