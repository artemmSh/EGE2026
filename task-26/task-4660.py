with open('files/26_4660.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

prices.sort(reverse=True)

ans2 = sum(prices) - sum(prices[-(N // 4):]) // 2
ans1 = sum(prices) - sum(prices[i] // 2 for i in range(3, len(prices), 4))

print(ans1, ans2)
