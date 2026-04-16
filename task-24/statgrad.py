from re import finditer
from string import ascii_uppercase

with open('') as file:
    data = file.readline()

ans = []
for i in '13579':
    pattern = rf'(?<={i})[A-Z]+(?={i})'
    matches = [match.group() for match in finditer(pattern, data)]
    for match in matches:
        cnt_vowels = 0
        cnt_cons = 0
        for char in ascii_uppercase:
            if char in 'EYUIOA': cnt_vowels += match.count(char)
            else: cnt_cons += match.count(char)
        if cnt_vowels == cnt_cons:
            ans.append([len(match), data.find(match), match])

print(max(ans)[1] - 1)
