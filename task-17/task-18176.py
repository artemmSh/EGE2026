with open('files/17_18176.txt') as file:
    data = [int(i) for i in file]
min_ends_with_4 = min(i for i in data if i > 0 and abs(i) % 10 == 4)
ans = []
for num in zip(data, data[1:], data[2:]):
    if sum(int(j) for i in num for j in str(abs(i))) == min_ends_with_4:
        ans.append(sum(num))
print(len(ans), max(ans))
