from re import finditer

with open('files/24_26077.txt') as file:
    data = file.readline()
pattern = r'G([^13579G]*[13579]){45}[^13579G]*'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))
