from re import *

with open('files/24_1975.txt') as file:
    data = file.readline()

pattern = r'[^P]*(P[^P]+)+[P]?'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))
