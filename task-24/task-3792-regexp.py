from re import *

with open('files/24_3792.txt') as file:
    data = file.readline()

pattern = r'[ABC]+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))
