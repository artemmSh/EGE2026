from itertools import *
# permutations - формирует все возможные перестановки элементов коллекции

alph = '122'
for val in permutations(alph):
    val = ''.join(val)
    print(val)

# product - формирует все возможные комбинации определенной длины
alph_2 = '123'
for val in product(alph_2, repeat=3):
    val = ''.join(val)
    print(val)

# enumerate - нумирует элементы последовательности начиная от start
alph_3 = '123'
res = enumerate(alph_3, start=1)
print(*res)
