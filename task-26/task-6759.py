with open('files/26_6759.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

prices.sort(reverse=True)
ans1 = sum(prices) - sum(prices[:(N // 3)])
ans2 = sum(prices) - sum(prices[2::3])
print(ans1, ans2)
