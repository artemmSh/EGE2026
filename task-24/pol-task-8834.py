from re import *
with open('files/24-371.txt') as file:
    data = file.readline()

pattern = r'(A[^A.]*){98}[.]'
matches = [match.group() for match in finditer(pattern, data)]
print(len(min(matches, key=len)))