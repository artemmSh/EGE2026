from re import *

# 1
with open('files/24_1146.txt') as file:
    data = file.readline()
cnt = 0
ans = 10 ** 20
for i in data:
    if i == 'D':
        cnt += 1
    elif cnt != 0:
        ans = min(ans, cnt)
        cnt = 0
if cnt != 0: ans = min(ans, cnt)
print(ans)

# 2
pattern = r'D+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(min(matches, key=len)))

# 3
for i in 'ABCEF':
    data = data.replace(i, ' ')
data = data.split()
print(len(min(data, key=len)))
