from itertools import *

end = []
dragon = []
for val in product('КОНЕЦ', repeat=5):
    end.append(''.join(val))
for val in product('ДРАКОН', repeat=5):
    dragon.append(''.join(val))

# оказывается xor для множеств возвращает не boolean, а симметрическую разность (множество)
print(len(set(dragon) ^ set(end)))

# то же самое
print(len(set(dragon).symmetric_difference(set(end))))

# это то же самое, только ручное
only_in_dragon = set(dragon) - set(end)
only_in_end = set(end) - set(dragon)
res = only_in_dragon.union(only_in_end)
print(len(res))

# это колхоз какой-то
for i in dragon:
    if i in end:
        while i in end:
            end.remove(i)
        while i in dragon:
            dragon.remove(i)

for i in end:
    if i in dragon:
        while i in end:
            end.remove(i)
        while i in dragon:
            dragon.remove(i)
print(len(end) + len(dragon))
