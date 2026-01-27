from string import printable as alph

with open('files/24_10724.txt') as file:
    data = file.readline().lower()

ans = 0
for l in range(len(data)):
    if data[l] in alph[1:16]:
        for r in range(l + 1, len(data)):
            if data[r] in alph[:16]:
                ans = max(ans, len(data[l:r + 1]))
            else:
                break
print(ans)
