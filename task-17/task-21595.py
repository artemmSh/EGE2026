with open('files/17_21595.txt') as file:
    data = [int(i) for i in file]

sq_len = sum(1000 <= abs(i) <= 9999 and abs(i) % 10 == 3 for i in data) ** 2
ans = []
for num in zip(data, data[1:], data[2:]):
    if sum(sorted(num)[1:]) > sq_len:
        ans.append(sum(num))
print(len(ans), abs(max(ans)))
