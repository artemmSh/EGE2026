with open('files/17_11236.txt') as file:
    data = [int(i) for i in file]

min_2_digits = min(i for i in data if 10 <= abs(i) <= 99)
max_4_digits_ends_with_1 = max(i for i in data if 1000 <= abs(i) <= 9999 and abs(i) % 10 == 1)
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    c1 = (num1 > min_2_digits ** 2) + (num2 > min_2_digits ** 2) + (num3 > min_2_digits ** 2) == 2
    c2 = (abs(num1) * abs(num2) * abs(num3)) % max_4_digits_ends_with_1 == 0
    if c1 and c2:
        ans.append(abs(num1) + abs(num2) + abs(num3))

print(len(ans), max(ans))

##############################


from math import prod

with open(r'.\files\17_11236.txt') as file:
    data = [int(i) for i in file]

min_2 = min(i for i in data if len(str(abs(i))) == 2) ** 2
max_1 = abs(max(i for i in data if str(i)[-1] == '1' and len(str(abs(i))) == 4))

ans = []
for num in zip(data, data[1:], data[2:]):
    u1 = sum(i > min_2 for i in num) == 2
    u2 = prod(map(abs, num)) % max_1 == 0
    if u1 and u2:
        ans.append(sum(map(abs, num)))
print(len(ans), max(ans))
