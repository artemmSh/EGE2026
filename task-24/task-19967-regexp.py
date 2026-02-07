from re import *

with open('files/24_19967.txt') as file:
    data = file.readline()

num = r'([1-9][0-9]*|0)'
pattern = fr'AFD({num}[+*])+{num}'
matches = [match.group() for match in finditer(pattern, data)]
print(matches)
print(len(max(matches, key=len)))
print(max(matches, key=len))
