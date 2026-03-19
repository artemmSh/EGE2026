with open('files/17_2997.txt') as file:
    data = [int(i) for i in file]

data_3 = [int(str(abs(i))[1]) for i in data if len(str(abs(i))) == 3]
most_common = max((data_3.count(i), i) for i in set(data_3))[1]
ans = []
for num in zip(data, data[1:]):
    c1 = sum(abs(i) % 10 == most_common for i in num) >= 1
    if c1:
        ans.append(sum(num))
print(len(ans), max(ans))
