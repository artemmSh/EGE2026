with open('files/17_9786.txt') as file:
    data = [int(i) for i in file]

four_digits = [i for i in data if 1000 <= abs(i) <= 9999]
max_ends_with_25 = max(i for i in data if abs(i) % 100 == 25)
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    c1 = (num1 in four_digits) + (num2 in four_digits) + (num3 in four_digits) <= 2
    c2 = num1 + num2 + num3 <= max_ends_with_25
    if c1 and c2:
        ans.append(num1 + num2 + num3)

print(len(ans), max(ans))
