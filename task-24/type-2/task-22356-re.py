from re import *

with open('../files/24_22356.txt') as file:
    data = file.readline()

pattern = r'[1-9A-B][0-9A-B]+[13579B]'

matches = [match.group() for match in finditer(pattern, data)]
print(data.index(max(matches, key=lambda x: (int(x, 12)))))
