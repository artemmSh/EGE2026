with open('files/26_4684.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

prices.sort(reverse=True)
ans1 = sum(prices) - sum(prices[5::6]) // 2
ans2 = sum(prices) - sum(prices[-(N // 6):]) // 2
print(ans1, ans2)
