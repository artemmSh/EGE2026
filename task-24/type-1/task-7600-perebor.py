with open(r'..\files\24_7600.txt') as file:
    data = file.readline()

forbidden = list()
for a in 'QRS':
    for b in 'QRS':
        forbidden.append(a + b)

l = 0
r = 0
ans = 0
while r < len(data):
    if r and data[r - 1:r + 1] in forbidden:
        l = r
    ans = max(ans, r - l + 1)
    r += 1
print(ans)
