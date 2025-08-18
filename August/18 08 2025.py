from re import *
with open('Regexp contest/regexp-practice-1.txt') as file:
    string = ''
    for i in file:
        string += i
pattern = r'\b[Cc][Aa][Tt]\b'
matches = finditer(pattern, string)
result = [i.group() for i in matches]
#print(result)

with open('Regexp contest/regexp-practice-2.txt') as file:
    string = file.readlines()
pattern = r'[Aa]'
#for line in string:
    #if match(pattern, line) is not None:
        #print(line)

with open('Regexp contest/regexp-practice-3.txt') as file:
    string = ''
    for i in file:
        string += i
pattern = r'[0-9]+(\.[0-9]+|[0-9]*)'
matches = finditer(pattern, string)
result = [i.group() for i in matches]
#print(result)

with open('Regexp contest/regexp-practice-4.txt') as file:
    string = ''
    for i in file:
        string += i
pattern = r'[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}'
matches = finditer(pattern, string)
result = [i.group() for i in matches]
#print(result)

with open('Regexp contest/regexp-practice-5.txt', encoding='utf-8') as file:
    string = ''
    for i in file:
        string += i
pattern = r'\b[A-ZА-ЯЁ][a-zа-яё]*\b'
matches = finditer(pattern, string)
result = [i.group() for i in matches]
#print(result)

with open('Regexp contest/regexp-practice-6.txt', encoding='utf-8') as file:
    string = ''
    for i in file:
        string += i
pattern = r'[A-ZА-ЯЁ]{2}-[0-9]{4}'
matches = finditer(pattern, string)
result = [i.group() for i in matches]
print(result)





