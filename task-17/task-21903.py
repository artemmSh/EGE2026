with open('files/17_21903.txt') as file:
    data = [int(i) for i in file]

min_ends_with_15_3_dig = min(i for i in data if 100 <= abs(i) <= 999 and abs(i) % 100 == 15) ** 2
ans = []
for num in zip(data, data[1:], data[2:]):
    s1 = all(str(i)[0].isdigit() or str(i)[0] == '-' for i in num)
    s2 = min(num) * max(num) > min_ends_with_15_3_dig
    if s1 and s2:
        ans.append(min(num) * max(num))
print(len(ans), min(ans))
