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

# Сумма цифр числа
# Двоичное число
R_1 = '101'
sum_1 = R_1.count('1')
# Число в любой системе до 10 включительно
num = '718'
summa = sum(map(int, num))
# Число в любой системе до 36 включительно
R_3 = 'AF7'
sum_3 = sum(map(lambda x: int(x, 36), R_3))

ans = []
R = 1
# Наибольший N при наибольшем R
ans.append([R, N])
print(max(ans))

# Наибольший N при наименьшем R
ans.append([R, N])
ans = sorted(ans, key=lambda x:(x[0], -x[1]))
print(ans[0])

# Наименьший N при наименьшем R
ans.append([R, N])
print(min(ans))

# Наименьший N при наибольшем R
ans.append([R, N])
ans = sorted(ans, key=lambda x:(-x[0], x[1]))
print(ans[0])
