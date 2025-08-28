from re import *

with open('24-337.txt') as file:
    data = file.readline()
pattern = r'[1-9A-D][0-9A-D]+'
matches = [match.group() for match in finditer(pattern, data)]
ans = []
for num in matches:
    if int(num, 14) % 98 == 0:
        ans.append(num)
    else:
        for l in range(len(num)):
            for r in range(l + 1, len(num) + 1):
                if num[l:r].lstrip('0') and int(num[l:r].lstrip('0'), 14) % 98 == 0:
                    ans.append(num[l:r].lstrip('0'))
                    break

print(len(max(ans, key=len)))
# 12345

# l = 0  r = 1 2 3 4 5
# l = 1  r = 2 3 4 5
# l = 2  r = 3 4 5
# l = 3  r = 4 5
# l = 4  r = 5


with open('24-314.txt') as file:
    data = file.readline()
number = r'([1-7][0-7]*|0)'
pattern = fr'(?<=F)({number}[+*])+{number}'
matches = [match.group() for match in finditer(pattern, data)]
ans = []
max_len = len(max(matches, key=len))
for i in matches:
    if len(i) == max_len:
        ans.append(i)
string = max(ans, key=eval)
pattern = r'[0-9]+'
new_string = sub(pattern, lambda x: str(int(x.group(), base = 8)), string)
print(eval(new_string))