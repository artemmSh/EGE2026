from re import *

with open('files/24_1273.txt') as file:
    data = file.readline()
pattern = r'(?<=XYZ).+?(?=XYZ)'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) + 4)
