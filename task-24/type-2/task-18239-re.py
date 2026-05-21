from re import *
with open('../files/24_18239.txt') as file:
    data = file.readline()
num = r'[1-9]+'
pattern = fr'\-?({num}\-)+{num}'
matches = [match.group() for match in finditer(pattern, data)]
ans = 0
for line in matches:
    if eval(line) > -20_000:
        ans = max(ans, len(line))
    else:
        pass
print(ans)
