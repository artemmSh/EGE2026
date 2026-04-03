from re import *

with open('24-334.txt') as file:
    data = file.readline()
pattern = r'[1-9AB][0-9AB]*[02468A]|[02468A]'
matches = finditer(pattern, data)
# print(len(max([i.group() for i in matches], key=len)))


with open('24-347.txt') as file:
    data = file.readline()
pattern = r'[1-7][0-7]*'
matches = [match.group() for match in finditer(pattern, data)]
ans = []
for num in matches:
    if int(num, base=8) % 13 == 0:
        ans.append(num)
    else:
        for l in range(0, len(num)):
            for r in range(1, len(num)- l):
                    num_sliced = num[l:-r]
                    if int(num_sliced, base = 8) % 13 == 0:
                        ans.append(num_sliced)
                        break
glist = []
max_num = len(max(ans))
for i in ans:
    if len(i) == max_num:
        glist.append(i)
glist = list(map(int, glist))
print(min(glist))
# 0123456789 [0:]
# 012345678 [0:-1]
# 01234567 [0:-2]
# 0123456 [0:-3]
# 012345 [0:-4]
# 01234 [0:-5]
# 0123 [0:-6]
# 012 [0:-7]
# 01 [0:-8]
# 0 [0:-9]

# 123456789 [1:]
# 12345678  [1:-1]
# 1234567 [1:-2]
# 123456 [1:-3]
# 12345 [1:-4]
# 1234 [1:-5]
# 123 [1:-6]
# 12 [1:-7]
# 1 [1:-8]
