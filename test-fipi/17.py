with open('files/1_17.txt') as file:
    data = [int(i) for i in file]

min_123_pos = min(i for i in data if i % 123 == 0 and i > 0)
ans = []
for nums in zip(data, data[1:]):
    if sum(nums) < min_123_pos:
        ans.append(sum(nums))
print(len(ans), abs(max(ans)))
