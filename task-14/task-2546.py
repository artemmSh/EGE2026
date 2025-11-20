from string import printable as alph

N = 4 ** 36 + 3 * 4 ** 20 + 4 ** 15 + 2 * 4 ** 7 + 49
different_symbols = set()

while N:
    different_symbols.add(alph[N % 16])
    N //= 16
print(len(different_symbols))
