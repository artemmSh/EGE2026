from re import *

# 1
with open('files/24_3228.txt') as file:
    data = file.readline()
cnt = 0
ans = 0
for i in range(len(data) - 1):
    if data[i:i + 2] in 'AC AB':
        cnt = 1
        for j in range(i + 2, len(data) - 1, 2):
            if data[j:j + 2] in 'AC AB':
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
print(ans)
# 2
pattern = r'(A[BC])+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 2)

# 3
for i in ['AB', 'AC']:
    data = data.replace(i, '*')
for i in 'ABC':
    data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))
