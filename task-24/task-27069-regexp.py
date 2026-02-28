from re import *

with open('files/24_27069.txt') as file:
    data = file.readline()

first_word = r'[A-Z][a-z]*'
word = r'[a-z]+'
space = r'\s'
end = r'[a-z]+[.]'
pattern = fr'{first_word}({space}{word})*{space}{end}'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len).split()))
