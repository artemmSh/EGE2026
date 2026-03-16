with open('files/17_2473.txt') as file:
    data = [int(i) for i in file]
ans = []
for num1, num2 in zip(data, data[1:]):
    c1 = num1 % 7 == 0 or num2 % 7 == 0
    c2 = abs(num1) % 10 == 3 or abs(num2) % 10 == 3
    if c1 and c2:
        ans.append(num1 + num2)
print(len(ans), min(ans))
