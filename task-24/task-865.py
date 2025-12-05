from re import *

with open('files/24_865.txt') as file:
    data = file.readline()

# 1
ans = 0
cnt = 0
for i in data:
    if i not in 'CF':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
print(ans)

# 2
pattern = r'[^CF]*'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

# 3
for i in 'CF':
    data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))
