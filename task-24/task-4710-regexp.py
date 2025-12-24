from re import *

with open('files/24_4710.txt') as file:
    data = file.readline()

pattern = r'([CDF][AO])+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 2)
