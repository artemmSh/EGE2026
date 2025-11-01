from re import *
with open('24.txt') as file:
    s = file.readline()
pattern = r'[02468][    S13579]*{35}'
matches = finditer(pattern, s)
a = [str(i) for i in matches]
print(len(a))
