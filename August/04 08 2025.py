#print(sum([int(i) for i in input().split()]))
# print(sum(map(int, input().split())))
num = int(input())

res = []
while num >= 2:
    res.append(num % 2)
    num//=2
res.append(num)
print(*res[::-1], sep='')


nums = input()
print(*map(lambda x: pow(int(x), 2), nums.split()))

