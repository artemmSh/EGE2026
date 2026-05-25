from re import sub

with open('../files/24_14510.txt') as file:
    data = file.readline()

pattern = r'[^EYUIOA]{2}[EYUIOA]'
data = sub(pattern, '*', data)
data = data.split('*')
ans = 100 ** 100
for i in range(1, len(data) - 498 - 1):
    line = '...' + '...'.join(data[i:i + 499]) + '...'
    ans = min(ans, len(line))
print(ans)
