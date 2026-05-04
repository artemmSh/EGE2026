from re import *

with open(r'..\files\24_4602.txt') as file:
    data = file.readline()

vow = 'AO'
con = 'BCD'

pattern = fr'([{con}][{vow}])+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 2)
