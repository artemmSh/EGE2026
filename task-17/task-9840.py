with open('files/17_9840.txt') as file:
    data = [int(i) for i in file]

four_digits = [i for i in data if 1000 <= abs(i) <= 9999]
max_ends_with_39_four_digits = max(i for i in four_digits if abs(i) % 100 == 39)
ans = []
for num1, num2 in zip(data, data[1:]):
    c1 = (num1 in four_digits) + (num2 in four_digits) == 1
    c2 = (num1 + num2) ** 2 <= max_ends_with_39_four_digits ** 2
    if c1 and c2:
        ans.append(num1 + num2)
print(len(ans), max(ans))
