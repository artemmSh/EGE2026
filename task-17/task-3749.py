from math import *

with open('files/17_3749.txt') as file:
    data = [int(i) for i in file]

sqrt_max = 3 * max(i for i in data if i ** 0.5 % 1 == 0)
ans = []
for num in zip(data, data[1:]):
    c1 = prod(num) ** 0.5 % 1 == 0
    c2 = any(i <= sqrt_max for i in num)
    if c1 and c2:
        ans.append(prod(num) ** 0.5)

print(len(ans), int(max(ans) + min(ans)))
