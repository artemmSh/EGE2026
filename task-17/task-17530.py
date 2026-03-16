with open('files/17_17530.txt') as file:
    data = [int(i) for i in file]
ans = []
for num1, num2 in zip(data, data[1:]):
    if num1 % 55 == min(data) or num2 % 55 == min(data):
        ans.append(num1 + num2)
print(len(ans), min(ans))
