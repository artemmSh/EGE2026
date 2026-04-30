from re import finditer

with open(r'..\..\files\24_2942.txt') as file:
    data = file.readline()

pattern = r'(A[BC])+'

matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)) // 2)
