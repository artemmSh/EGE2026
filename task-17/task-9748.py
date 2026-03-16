with open('files/17_9748.txt') as file:
    data = [int(i) for i in file]

max_18 = max(i for i in data if i % 100 == 15)

ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    c1 = (1000 <= num1 <= 9999) + (1000 <= num2 <= 9999) + (1000 <= num3 <= 9999) == 1
    c2 = num1 + num2 + num3 >= max_18
    if c1 and c2:
        ans.append(num1 + num2 + num3)
print(len(ans), max(ans))
