with open('files/24_11667.txt') as file:
    data = file.readline()

data2 = data.split('INFINITY')
ans = 0
for i in range(len(data2) - 1000):
    text = 'INFINITY'.join(data2[i:i + 1001])
    if i == 0 or i == len(data) - 1001:
        ans = max(ans, len(text) + 7)
    else:
        ans = max(ans, len(text) + 14)
print(ans)
