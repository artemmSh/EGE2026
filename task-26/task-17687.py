with open('files/26_17687.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

prices.sort(reverse=True)
ans1 = sum(prices) - sum(prices[:(N // 9)])
ans2 = sum(prices) - sum(prices[8::9])
print(ans1, ans2)