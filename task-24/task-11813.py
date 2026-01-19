from string import ascii_uppercase as alph
from re import *

with open('files/24_11813.txt') as file:
    data = file.readline()
vow = 'AEYUIO'
con = ''
for i in alph:
    if i not in vow:
        con += i

pattern = fr'({[vow]}{[con]})+|({[con]}{[vow]})+'

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))