# Порядок выполнения операций в алгебре логики
# Инверсия - not
# Конъюнкция - and
# Дизъюнкция - or
# Импликация - <=
# Эквивалентность - ==
# Порядок выполнения операций в Python
# ()
# **
# /, //, %, *
# +, -
# ==, !=, <, <=, >, >=
# not
# and
# or

# Решение лесенкой
# for a in 0, 1:
#     for b in 0, 1:
#         for c in 0, 1:
#             for d in 0, 1:
#                 f = (not a and not b) or (b == c) or d
#                 # Все строки истинны
#                 if f:
#                     print(a, b, c, d)
#                 # Все строки ложны
#                 if not f:
#                     print(a, b, c, d)
#                 # Строки вперемешку
#                 print(a, b, c, d)

# args
# def f1(a, b, c):
#     return a + b + c
#
#
# test = [1, 2, 3]
# print(f1(*test))
#
#
# # kwargs
# def f2(a, b):
#     return a / b
#
#
# test2 = {'a': 5, 'b': 2, 'a': 7}
# print(f2(**test2))
#
# p = ('x', 'y', 'z', 'w')
# t = (1, 0, 1, 1)
# print(*dict(zip(p, t)))

# autocode
# from itertools import *
#
#
# def f(w, x, y, z):
#     return (x or y) and not (y == z) and not w
#
#
# for i in product((0, 1), repeat=4):
#     table = [
#         (1, i[0], 1, i[1]),
#         (0, 1, i[2], 0),
#         (i[3], 1, 1, 0)
#     ]
#     if len(set(table)) == len(table):
#         for p in permutations('wxyz'):
#             if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
#                 print(*p, sep='')
