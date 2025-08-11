import re
from itertools import count
from re import findall

with open('reg_exp_task_1.txt') as file:
    string = file.readline()

pattern = r'\d+'
matches = findall(pattern, string)
#print(matches)

with open('reg_exp_task_2.txt') as file:
    string = file.readline()
pattern = r'-?\d+\.?\d*'
matches = findall(pattern, string)
#print(matches)

string = 'abbbbbcc'
pattern = 'a+b{2,}c+'
matches = re.sub(pattern, 'HELLO', string)
#print(matches)

with open('reg_exp_task_4.txt') as file:
    string = file.readline()
pattern = r'[a-zA-Z0-9]*@[a-zA-Z0-9]*.[a-z]+' # \w+
matches = findall(pattern, string)
#print(matches)

with open('2400.txt') as file:
    string = file.readline()
pattern3 = r'((PNO)|(NPO))+'
matches3 = [match.group() for match in re.finditer(pattern3, string)]
print(len(max(matches3, key=len))//3)



