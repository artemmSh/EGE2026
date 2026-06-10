from re import *

with open('files/24_4682.txt') as file:
    data = file.readline()

pattern = r'([AE][BCD])+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 2)
