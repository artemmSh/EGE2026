from string import ascii_uppercase as alph

with open('files/24_1428.txt') as file:
    data = file.readline()

data = data.replace('XY', 'X Y').replace('XZ', 'X Z')
data = data.split()
print(len(max(data, key=len)))
