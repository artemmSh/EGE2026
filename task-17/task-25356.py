with open('files/17_25356.txt') as file:
    data = [int(i) for i in file]

four_digits = [i for i in data if 1000 <= abs(i) <= 9999]
max_30 = max(i for i in data if abs(i) % 100 == 30)
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    c1 = not any(i in four_digits for i in (num1, num2, num3))
    c2 = (num1 + num2 + num3) > max_30
    if c1 and c2:
        ans.append(num1 + num2 + num3)
print(len(ans), max(ans))
