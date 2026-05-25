from re import *

with open('../files/24_28943.txt') as file:
    data = file.readline()
data = data.replace('20', '&')
pattern = r'(20([^EYUIOA]?[^0EYUIOA])?){26}[EYUIOA]'
pattern = r'(&[^EYUIOA&]*){26}[EYUIOA]'
matches = [match.group() for match in finditer(pattern, data)]
print(len(min(matches, key=len)) + 26)