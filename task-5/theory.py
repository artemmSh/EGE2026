# Системы счисления

#  Двоичная система
N = 25
print(bin(N)[2:])
print(f'{N:b}')

# Восьмеричная система
print(oct(N)[2:])
print(f'{N:o}')

# Шестнадцатеричная система
print(hex(N)[2:])
print(f'{N:x}')


# Перевод в любую систему (2 <= sys <= 9)

def convert(num):
    res = ''
    while num:
        res += str(num % 3)
        num //= 3
    return res[::-1]


# Перевод в любую систему (2 <= sys <= 36)
from string import printable as alph


def convert(num):
    res = ''
    while num:
        res += alph[num % 3]
        num //= 3
    return res[::-1]

# Перевод в десятичную систему
bin_num = '101'
oct_num = '765'
tri_num = '1201'
print(int(bin_num, 2))
print(int(oct_num, 8))
print(int(tri_num, 3))
