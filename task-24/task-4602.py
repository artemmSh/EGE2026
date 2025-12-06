from re import *
from string import ascii_uppercase

# 1
with open('files/24_4602.txt') as file:
    data = file.readline()
combinations = []
vowels = 'EYUIOA'
for i in ascii_uppercase:
    for j in vowels:
        if i not in vowels:
            combinations.append(i + j)

cnt = 0
ans = 0
for i in range(len(data) - 1):
    if data[i:i + 2] in combinations:
        cnt = 1
        for j in range(i + 2, len(data) - 1, 2):
            if data[j:j + 2] in combinations:
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
print(ans)
# 2
vowels = 'EYUIOA'
pattern = fr'([^{vowels}][{vowels}])+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 2)

# 3
for i in ascii_uppercase:
    if i in vowels:
        data = data.replace(i, '*')
    else:
        data = data.replace(i, '+')

data = data.replace('+*', '!')
data = data.replace('+', ' ')
data = data.replace('*', ' ')
data = data.split()

print(len(max(data, key=len)))
