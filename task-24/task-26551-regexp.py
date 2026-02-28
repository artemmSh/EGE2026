from re import *

with open('files/24_26551.txt') as file:
    data = file.readline()

pattern = r'[1-9A-E][0-9A-E]*[02468ACE]'

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))
