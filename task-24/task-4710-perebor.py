from string import ascii_uppercase as alph

with open('files/24_4710.txt') as file:
    data = file.readline()

vowels = 'EYUIOA'
pairs = []
for i in alph:
    for j in vowels:
        if i not in vowels:
            pairs.append(i + j)
ans = 0
for i in range(len(data) - 1):
    if data[i:i + 2] in pairs:
        cnt = 1
        for j in range(i + 2, len(data) - 1, 2):
            if data[j:j + 2] in pairs:
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
print(ans)
