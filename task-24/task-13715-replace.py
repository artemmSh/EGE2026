with open('files/24_13715.txt') as file:
    data = file.readline()

data2 = data.split('AB')
ans = 0
for i in range(len(data2) - 50):
    text = 'AB'.join(data2[i:i + 51])
    if data.index(text) == 0 or data[::-1].index(text[::-1]) == 0:
        ans = max(ans, len(text) + 1)
    else:
        ans = max(ans, len(text) + 2)
print(ans)
