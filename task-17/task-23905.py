with open('files/17_23905.txt') as file:
    data = [int(i) for i in file]

max_37 = max(i for i in data if i % 100 == 37)
ans = []
for nums in zip(data, data[1:], data[2:], data[3:]):
    s1 = sum(num > max_37 for num in nums) == 2
    s2 = sum(num > 9 and str(num)[-2:] == str(num)[-2:][::-1] for num in nums) == 1
    if s1 and s2:
        ans.append(sum(num for num in nums if num > 9 and str(num)[-2:] == str(num)[-2:][::-1]))
print(len(ans), sum(ans))
