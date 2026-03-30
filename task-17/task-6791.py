with open('files/17_6791.txt') as file:
    data = [int(i) for i in file]

ends_with_68 = [i for i in data if abs(i) % 100 == 68]
sq_min_68 = min(ends_with_68) ** 2
ans = []
for num in zip(data, data[1:]):
    s1 = sum(i in ends_with_68 for i in num) == 1
    s2 = sum(i ** 2 for i in num) >= sq_min_68
    if s1 and s2:
        ans.append(sum(i ** 2 for i in num))
print(len(ans), max(ans))
