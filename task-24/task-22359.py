from re import *
from string import printable as alph

with open('files/24_22359.txt') as file:
    data = file.readline()

alph = alph[:15].upper()

pattern = fr'[{alph}^0][{alph}]+'

matches = [match.group() for match in finditer(pattern, data) if int(match.group(), 15) % 5 == 0]
max_str = (max(matches, key=lambda x: int(x, 15)))
print(data.index(max_str) + len(max_str) - 1)
