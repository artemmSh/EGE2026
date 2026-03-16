with open('files/17_17558.txt') as file:
    data = [int(i) for i in file]

div_32 = [i for i in data if abs(i) % 32 == 0]
ans = []
for num1, num2 in zip(data, data[1:]):
    c1 = num1 < 0 or num2 < 0
    c2 = (num1 + num2) < len(div_32)
    if c1 and c2:
        ans.append(num1 + num2)
print(len(ans), max(ans))
