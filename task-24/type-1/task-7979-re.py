from re import *

with open('../files/24-314.txt') as file:
    data = file.readline()
num = r'([1-7][0-7]*|0)'
pattern = fr'(?<=F)({num}[+*])+{num}'
matches = [match.group() for match in finditer(pattern, data)]
ans = []
for match in matches:
    match = match.replace('*', ' * ')
    match = match.replace('+', ' + ')
    match = match.split()
    match = [str(int(match[i], 8)) if i % 2 == 0 else match[i] for i in range(len(match))]
    ans.append([len(match), eval(''.join(match))])

print(max(ans)[1])
