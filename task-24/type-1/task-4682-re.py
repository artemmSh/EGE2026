from string import ascii_uppercase as alph
from re import *

with open(r'..\files\24_4682.txt') as file:
    data = file.readline()

vow = 'EYUIOA'
con = ''.join(i for i in alph if i not in vow)

pattern = fr'([{vow}][{con}])+'

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 2)
