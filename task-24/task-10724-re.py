from re import *
from string import printable as alph

with open('files/24_10724.txt') as file:
    data = file.readline().lower()

pattern = fr'[{alph[1:16]}][{alph[:16]}]*'

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))
