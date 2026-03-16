with open('files/17_17636.txt') as file:
    data = [int(i) for i in file]

three_digits_ends_with_3 = [i for i in data if 100 <= abs(i) <= 999 and abs(i) % 10 == 3]
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    c1 = (num1 in three_digits_ends_with_3) or (num2 in three_digits_ends_with_3) or (num3 in three_digits_ends_with_3)
    c2 = (num1 + num2 + num3) < max(three_digits_ends_with_3)
    if c1 and c2:
        ans.append(num1 + num2 + num3)
print(len(ans), max(ans))
