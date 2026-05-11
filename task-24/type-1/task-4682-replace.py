from string import ascii_uppercase as alph

with open(r'..\files\24_4682.txt') as file:
    data = file.readline()

vow = 'EYUIOA'
con = ''.join(i for i in alph if i not in vow)
combs = [v + c for v in vow for c in con]
for i in combs:
    data = data.replace(i, '*')

for i in alph:
    data = data.replace(i, ' ')

data = data.split()

print(max(map(len, data)))
