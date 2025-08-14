from re import *
with open('2405.txt') as file:
    string = file.readline()

pattern = r'(LMN|MN|N)?(KLMN)+(KLM|KL|K)?'
matches = finditer(pattern, string)
res = [i.group() for i in matches]
#print(len(max(res, key=len)))

with open('2416.txt') as file:
    string = file.readline()
pattern = r'([AE][BCD])+'
matches = finditer(pattern, string)
res = [i.group() for i in matches]
#print(len(max(res, key=len))//2)

with open('2402.txt') as file:
    string = file.readline()
number = r'([789][0789]*|0)'
pattern = fr'({number}[-\*])+{number}'
matches = finditer(pattern, string)
res = [i.group() for i in matches]
print(len(max(res, key=len)))




