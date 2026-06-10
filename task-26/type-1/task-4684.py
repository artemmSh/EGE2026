with open('../files/26_4684.txt') as file:
    N = int(file.readline())
    goods = [int(i) for i in file]

goods.sort()

ans1 = sum(goods) - sum(goods[::-1][5::6]) // 2
ans2 = sum(goods) - sum(goods[:(N // 6)]) // 2

print(ans1, ans2)
