import math


def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


with open('files/17_9993.txt') as file:
    data = [int(i) for i in file]

max_ends_with_17 = max(i for i in data if abs(i) % 100 == 17)
ans = []
for num in zip(data, data[1:]):
    c1 = sum(is_prime(i) for i in num) == 1
    c2 = abs(sum(num)) % max_ends_with_17 == 0
    if c1 and c2:
        ans.append(math.prod(num))
print(len(ans), max(ans))
