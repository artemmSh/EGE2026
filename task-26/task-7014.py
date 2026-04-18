with open('files/26_7014.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

max_revenue_per_day = 0
sum_revenue = 0

while prices:
    max_price = max(prices)
    pos = prices.index(max_price)
    revenue_per_day = max_price * (pos + 1)
    sum_revenue += revenue_per_day
    max_revenue_per_day = max(max_revenue_per_day, revenue_per_day)
    prices = prices[pos + 1:]
print(sum_revenue, max_revenue_per_day)
