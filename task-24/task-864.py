from re import *

with open('files/24_864.txt') as file:
    data = file.readline()

# 1
cnt = 0
ans = 0
for i in data:
    if i not in 'AE':
        cnt += 1
    else:
        ans = max(cnt, ans)
        cnt = 0
print(ans)

# 2
pattern = r'[^AE]*'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))

# 3
for i in 'AE':
    data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))
