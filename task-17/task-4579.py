with open('files/17_4597.txt') as file:
    data = [int(i) for i in file]

minimum = min(data)

ans = []
for num1, num2 in zip(data, data[1:]):
    c1 = num1 % 117 == minimum
    c2 = num2 % 117 == minimum
    if c1 + c2 >= 1:
        ans.append(num1 + num2)
print(len(ans), max(ans))
