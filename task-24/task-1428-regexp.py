from re import *

with open('files/24_1428.txt') as file:
    data = file.readline()

pattern = r'(^|(?<=(XY|XZ))).+?($|(?=(XY|XZ)))'
matches = [match.group() for match in finditer(pattern, data)]
ans = 0
for match in finditer(pattern, data):
    if match.span()[0] in [0, len(match.group()) - 1]:
        ans = max(ans, len(match.group()) + 1)
    else:
        ans = max(ans, len(match.group()) + 2)
print(ans)
