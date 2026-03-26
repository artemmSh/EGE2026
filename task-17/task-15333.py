with open('files/17_15333.txt') as file:
    data = [int(i) for i in file]

max_div_19 = max(i for i in data if i % 19 == 0)
ans = []
for num in zip(data, data[1:]):
    if any(i > max_div_19 for i in num):
        ans.append(sum(num))
print(len(ans), max(ans))
