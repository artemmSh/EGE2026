from re import *

with open('files/24_1874.txt') as file:
    data = file.readline()

# 1
cnt = 1
ans = 0
for i in range(len(data) - 1):
    if data[i:i + 2] != 'QW':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1
ans = max(ans, cnt)
print(ans)
# 2
pattern = r'((?<=^)|(?<=QW)).+?((?=QW)|(?=$))'  # Я не знаю как сделать чтоб под любую строку. В данном случае работает а, так вообщевпапавпджюложыфтоаилпслчапми
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))
# 3
data = data.replace('QW', 'Q W')
data = data.split()
print(len(max(data, key=len)))
