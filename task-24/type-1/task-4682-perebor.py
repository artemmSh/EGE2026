from string import ascii_uppercase as alph

with open(r'..\files\24_4682.txt') as file:
    data = file.readline()

vow = 'EYUIOA'
con = ''.join(i for i in alph if i not in vow)

ans = 0
for i in range(len(data) - 1):
    if data[i] in vow and data[i + 1] in con:
        cnt = 1
        for j in range(i + 2, len(data) - 1, 2):
            if data[j] in vow and data[j + 1] in con:
                cnt += 1
            else:
                break
            ans = max(ans, cnt)

print(ans)