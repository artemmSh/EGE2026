from re import *

with open('files/24_16388.txt') as file:
    data = file.readline()

#1

#2
pattern = r'L?M?N?(KLMN)+K?L?M?'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

#3
