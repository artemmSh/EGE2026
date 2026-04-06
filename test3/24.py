with open('files/24 (2).txt') as file:
    data = file.readline()

data = data.split('Z')
ans = 10 ** 30
for i in range(len(data) - 268):
    line = 'Z'.join(data[i:i + 269])
    ans = min(ans, len(line) + 2)
print(ans)  # 1067
# ans = 10 ** 100
# for l in range(len(data)):
#     if data[l] == 'Z':
#         cnt_Z = 1
#         for r in range(l + 1, len(data)):
#             if data[r] == 'Z':
#                 cnt_Z += 1
#             if cnt_Z == 270:
#                 ans = min(ans, len(data[l:r + 1]))
#                 break
# print(ans) # 1058
