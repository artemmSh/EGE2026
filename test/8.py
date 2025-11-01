from itertools import *
num = 0
for i in product(sorted('АЛГОРИТМ'), repeat=5):
    num +=1
    s = ''.join(i)
    if num % 2 == 0 and s[0] not in 'АГ' and s.count('Р') >=2:
        print(num, s)
        break
