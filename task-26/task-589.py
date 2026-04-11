with open('files/26_589.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

prices.sort()
sorted_prices = list()

for i, cheap in enumerate(prices):
    if cheap:
        sorted_prices.append(cheap)
        for j, exp in enumerate(prices[::-1]):
            if exp and (cheap - 1) // 500 == (exp - 1) // 500:
                sorted_prices.append(exp)
                prices[i], prices[len(prices) - j - 1] = 0, 0
                break
        else:
            sorted_prices.remove(cheap)

ans1 = sum(sorted_prices[::2]) // 2
ans2 = sorted_prices[-2] // 2
print(ans1, ans2)
