with open('files/17 (2).txt') as file:
    data = [int(i) for i in file]

two_digits = [i for i in data if 10 <= i <= 99]
max_two_digits = max(two_digits)
ans = []
for nums in zip(data, data[1:]):
    s1 = sum(i in two_digits for i in nums) == 1
    s2 = sum(nums) % max_two_digits == 0
    if s1 and s2:
        ans.append(sum(nums))
print(len(ans), max(ans))
