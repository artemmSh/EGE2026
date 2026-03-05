from string import *

alph = digits + ascii_uppercase

for p in range(alph.index(max('KOTGOLODNIMEEOW')), 100):
    num1 = int('t', 36) * p ** 0 + int('o', 36) * p ** 1 + int('k', 36) * p ** 2 + int('i', 36) * p ** 0 + int('n', 36) * p ** 1 + int('d', 36) * p ** 2 + int('o', 36) * p ** 3 + int('l', 36) * p ** 4 + int('o', 36) * p ** 5 + int('g', 36) * p ** 6
    num2 = (int('w', 36) * p ** 0 + int('o', 36) * p ** 1 + int('e', 36) * p ** 2 + int('e', 36) * p ** 3 + int('m', 36) * p ** 4) * 1 * p ** 2 - 20194023088
    if num1 == num2:
        print(int('r', 36) * p ** 0 + int('r', 36) * p ** 1 + int('u', 36) * p ** 2 + int('p', 36) * p ** 3)
        break
