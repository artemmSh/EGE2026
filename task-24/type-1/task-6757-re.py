from re import *

with open('../files/24_6757.txt') as file:
    data = file.readline()

pattern = '(CFE|FCE)+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 3)
