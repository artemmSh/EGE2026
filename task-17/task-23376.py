with open('files/17_23376.txt') as file:
    data = [int(i) for i in file]

five_digits = [i for i in data if 9999 < abs(i) < 100000]
max_37 = max(i for i in five_digits if str(i)[-2:] == '37') ** 2
ans = list()
for nums in zip(data, data[1:]):
    s1 = sum(num in five_digits for num in nums) == 1
    s2 = sum(nums) ** 2 > max_37
    if s1 and s2:
        ans.append(sum(nums))
print(len(ans), max(ans))
