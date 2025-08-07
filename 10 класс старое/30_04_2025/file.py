int()  # целые числа
float()  # дробные числа
complex()  # комплексные числа
bool()  # логический тип
# Итерируемый обйект, коллекция
# последовательности
list()  # список
str()  # строка
tuple()  # кортеж
dict()  # словарь
set()  # множества

# Множество - тип коллекции, который содержит уникальные неиндексируемые элементы

my_set = {1, 2, 3}
# add() - это добавление элемента в множество
# принимает любой тип данных, кроме списков и словарей
# возвращает ничего
my_set.add(4)
print(my_set)

# remove() - удаление определенного элемента из множества
# если передать элемент, которого не существует в множестве, будет ошибка
# возвращает ничего
my_set.remove(1)
print(my_set)

# обйеденение множеств
my_set2 = {1, 2, 3}
union_set = my_set.union(my_set2)
print(union_set)

# разность множеств
diff_set = my_set2.difference(my_set)
print(diff_set)

# симметричная разность
sym_diff_set = my_set.symmetric_difference(my_set2)
print(sym_diff_set)

# отношение между множествами
# issubset() - проверяет, является ли одно множество подмножеством другого
sub_set = {3, 4, 5}
super_set = {1, 2, 3, 4, 5}
print(super_set.issubset(sub_set))
print(sub_set.issubset(super_set))

# issuperset() - проверяет, является ли одно множество надмножеством другого

print(super_set.issuperset(sub_set))
print(sub_set.issuperset(super_set))