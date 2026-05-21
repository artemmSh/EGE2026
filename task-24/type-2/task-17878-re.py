from re import *

with open('../files/24_17878.txt') as file:
    data = file.readline()
num = r'(0|[6789][06789]*)'
pattern = fr'({num}[-*])+{num}'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))
