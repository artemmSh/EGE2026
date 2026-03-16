with open('files/17_12249.txt') as file:
    data = [int(i) for i in file]

ends_with_3 = [i for i in data if abs(i) % 10 == 3]
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    c1 = (num1 in ends_with_3) or (num2 in ends_with_3) or (num3 in ends_with_3)
    c2 = (num1 + num2 + num3) <= max(i for i in ends_with_3 if 10000 <= abs(i) <= 99999)
    if c1 and c2:
        ans.append(num1 + num2 + num3)
print(len(ans), max(ans))
